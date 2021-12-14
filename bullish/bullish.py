import base64
import datetime as dt
from hashlib import sha256
import json
import requests
# import time
import typing
import logging

from bullish.objects.account import AccountResponse
from bullish.objects.error import Error
from bullish.objects.general import ExchangeTime, Nonce
from bullish.objects.market import Market, MarketCandle, MarketOrderBook, MarketTick, MarketTrade
from bullish.objects.order import OrderCreate, OrderCancel, OrderPageResponse, OrderResult, OrderResponse
from bullish.objects.position import PositionResponse
from bullish.objects.trade import TradePageResponse, TradeResponse
from bullish.objects.spot import SpotResponse


from eosio_signer import EOSIOKey


class Bullish:

    _log = logging.getLogger(__name__)

    # endpoints 
    _endpoints = {
        'margin': '/trading-api/v1/accounts/margin',
        'markets': '/trading-api/v1/markets',
        'nonce': '/trading-api/v1/nonce',
        'orders': '/trading-api/v1/orders',
        'position': '/trading-api/v1/position',
        'trades': '/trading-api/v1/trades',
        'time': '/trading-api/v1/time',
        'spot': '/trading-api/v1/accounts/spot',
        'login': '/trading-api/v1/users/login',
    }

    _defaultHeader = {'Content-type': 'application/json', }

    def __init__(self, hostname: str, pKey: str, metadata: str, timeout: int = 5, verify: bool = True):
        ''' '''
        self._hostname = hostname
        # decode metadata
        self._log.debug(base64.b64decode(metadata))
        self._accountId = json.loads(base64.b64decode(metadata))['accountId']
        self._key = EOSIOKey(pKey)
        # setup session
        self._session = requests.Session()
        self._verify = verify
        self._session.headers.update(self._defaultHeader)
        self._timeout = timeout
        # 
        self._token = ''
        self._authorizer = ''
        self._nonce = 0

    def _process_response(self, resp):
        # process Bullish specific errors
        if(resp.status_code == 500 or resp.status_code == 400):
            self._log.error(resp.text)
            Error(resp.json()).raise_error()
        self._log.debug(resp.text)
        resp.raise_for_status()
        return resp.json()

    def _get_data(self, url: str, headers=None, params: dict = {}) -> dict:
        ''' '''
        resp = self._session.get(
            f'{self._hostname}{url}', headers=headers, params=params)
        return self._process_response(resp)

    def _sign(self, body: dict) -> str:
        ''' '''
        payload = f'{json.dumps(body, separators=(",", ":"))}'.encode("utf-8")
        digest = sha256(payload.rstrip()).hexdigest()
        return self._key.sign(digest)

    def _generate_signed_info(self, command: dict) -> dict:
        ''' '''
        timestamp = int(dt.datetime.now().timestamp())
        nonce = int(timestamp * 1000000)
        ts = int(nonce / 1000)
        # create body
        body = {
            'timestamp': f'{ts}',
            'nonce': f'{nonce}',
            'authorizer': self._authorizer,
            'command': command
        } 
        self._log.debug(body)
        # generate headers
        headers = {}
        headers['BX-SIGNATURE'] = self._sign(body)
        headers['BX-TIMESTAMP'] = f'{ts}'
        headers['BX-NONCE'] = f'{nonce}'
        return (headers, body)

    def _post_data(self, url: str, body: dict, sign: bool = True) -> dict:
        ''' '''
        headers = {}
        if sign:
            (headers, body) = self._generate_signed_info(body)
        self._log.debug(body)
        resp = self._session.post(
            f'{self._hostname}{url}', json=body, headers=headers, verify=self._verify)
        return self._process_response(resp)

    def _delete_data(self, url: str, body: dict, params: dict = None, sign: bool = True) -> dict:
        ''' '''
        headers = {}
        if sign:
            headers, body = self._generate_signed_info(body)
        resp = self._session.delete(
            f'{self._hostname}{url}', json=body, params=params, headers=headers)
        return self._process_response(resp)

    def login(self):
        ''' '''
        # TODO this doesn't seem right. Should use `utcnow`
        # ts = int(dt.datetime.utcnow().timestamp())
        ts = int(dt.datetime.now().timestamp())
        nonce = int(dt.datetime.now().timestamp())
        payload = {
            'accountId': f'{self._accountId}', #
            'nonce': nonce,
            'expirationTime': ts + 300,
            'biometricsUsed': False,           # always false
            'sessionKey': None
        }
        self._log.debug(payload)

        signature = self._sign(payload)
        body = {
            'publicKey': self._key.to_public(),
            'signature': signature,
            'loginPayload': payload
        }
        resp = self._post_data(self._endpoints['login'], body=body, sign=False)
        self._token = resp['token']
        self._authorizer = resp['authorizer']
        # set bearer in the headers
        self._session.headers.update({'Authorization': f'Bearer {self._token}'})

    # TIME
    def get_exchange_time(self) -> ExchangeTime:
        '''
        Public API for reading time data
        '''
        ex_time = self._get_data(self._endpoints["time"])
        return ExchangeTime(ex_time)

    # NONCE
    def get_nonce(self) -> Nonce:
        '''
        Get current nonce range
        '''
        nonce = self._get_data(self._endpoints["nonce"])
        if nonce['lowerBound'] > self._nonce:
            self._nonce = nonce['lowerBound']
        return Nonce(nonce)

    # MARKET-DATA
    def _get_markets(self, symbol: str = '') -> typing.Union[typing.List[Market], Market]:
        ''' 
        Get Markets
        '''
        url = self._endpoints["markets"]
        if symbol:
            url += f"/{symbol}"
        market_resp = self._get_data(url)
        if type(market_resp) == list:
            market_list = []
            for m in market_resp:
                market_list.append(Market(m))
            return market_list
        else:
            return Market(market_resp)

    def get_market(self, symbol: str) -> Market:
        ''' 
        Get Market by Symbol
        '''
        return self._get_markets(symbol)

    def get_markets(self) ->typing.List[Market]:
        ''' 
        Get All Markets
        '''
        return self._get_markets()

    def get_market_candle(self, symbol, startTime: dt.datetime = None, endTime: dt.datetime = None, timeBucket: str = "1m") -> typing.List[MarketCandle]:
        '''
        Get Current OHLCV Candle by Market Symbol
        '''
        # default end/start timestamps
        endTs = dt.datetime.utcnow()
        startTs = dt.datetime.utcnow() - dt.timedelta(hours=1)
        # set timestamps if given
        if startTime:
            startTs = startTime
        if endTime:
            endTs = endTime

        def convert_time(t: dt.datetime):
            return t.replace().isoformat(' ', 'milliseconds').replace(' ', 'T') + 'Z'
        # create url
        gte = convert_time(startTs)
        lte = convert_time(endTs)
        # add params
        params = {
            'createdAtDatetime[gte]': gte,
            'createdAtDatetime[lte]': lte,
            'timeBucket': timeBucket
        }
        url = f'{self._endpoints["markets"]}/{symbol}/candle'
        # get and process candle data
        candle_resp = self._get_data(url, params=params)
        candle_list = []
        for candle in candle_resp:
            candle_list.append(MarketCandle(candle))
        return candle_list

    def get_market_orderbook(self, symbol: str) -> MarketOrderBook:
        ''' 
        Get OrderBook by Market Symbol
        '''
        order_resp = self._get_data(
            f'{self._endpoints["markets"]}/{symbol}/orderbook/hybrid')
        return MarketOrderBook(order_resp)

    def get_market_tick(self, symbol: str) -> MarketTick:
        ''' 
        Get Current Tick by Market Symbol
        '''
        tick_resp = self._get_data(
            f'{self._endpoints["markets"]}/{symbol}/tick')
        return MarketTick(tick_resp)

    def get_market_trade(self, symbol: str) -> typing.List[MarketTrade]:
        '''
        Get Trades by Market Symbol
        '''
        trade_resp = self._get_data(
            f'{self._endpoints["markets"]}/{symbol}/trades')
        trades = []
        for trade in trade_resp:
            trades.append(MarketTrade(trade))
        return trades

    # ORDERS
    def get_orders(self, _metadata:bool = False, **kwargs) -> OrderPageResponse:
        ''' 
        Gets the orders list based on specified filters.
            - supports pagination
            - supports filtering on symbol, orderId, side, status=OPEN
        '''
        if _metadata:
            kwargs['_metaData'] = "true"
        # create url
        orders_resp = self._get_data(
            self._endpoints['orders'], params=kwargs)
        
        if not _metadata:
            self._log.debug('Paging is enabled')
            orders_data = orders_resp
            # create order page response data structure
            orders_resp = {
                'data': orders_data,
                'links': {
                    'next': '',
                    'previous': ''
                }
            }
        orders = OrderPageResponse(**orders_resp)
        return orders

    def get_order_by_id(self, orderId: str) -> OrderResult:
        '''
        Get Order by ID
        '''
        # create url
        order_resp = self._get_data(
            f'{self._endpoints["orders"]}/{orderId}')
        return OrderResult(**order_resp)

    def create_order(self, order: OrderCreate) -> OrderResponse:
        '''
        Create Order
        '''
        resp = self._post_data(
            self._endpoints['orders'], order.to_dict(), sign=True)
        return OrderResponse(**resp)

    def cancel_order(self, order: OrderCancel) -> OrderResponse:
        '''
        Delete Order
        '''
        resp = self._delete_data(
            self._endpoints['orders'], body=order.to_dict(), params=order.to_dict())
        return OrderResponse(**resp)

    # trades
    def get_trades(self, _metadata: bool = False, **kwargs) -> typing.List[TradeResponse]:
        '''
        Get Trades
            - Supports pagination
            - Supports filtering on symbol, orderId, tradeId
        '''
        if _metadata:
            kwargs['_metaData'] = "true"
        trades = []
        trade_resp = self._get_data(
            self._endpoints['trades'], params=kwargs)
        if not _metadata:
            self._log.debug('Paging is enabled')
            trades_data = trade_resp
            # create trade page response data structure
            trade_resp = {
                'data': trades_data,
                'links': {
                    'next': '',
                    'previous': ''
                }
            }
        trades = TradePageResponse(**trade_resp)
        return trades

    def get_trade_by_id(self, tradeId: int) -> TradeResponse:
        '''
        Get Trade by ID
        '''
        trade_resp = self._get_data(
            f'{self._endpoints["trades"]}/{tradeId}')
        return TradeResponse(**trade_resp)


    def _get_object_data(self, endpoint: str, obj, symbol: str = ''):
        '''
        get a list or single object
        '''
        url = endpoint
        if symbol:
            url += f'/{symbol}'
        resp = self._get_data(url)
        if type(resp) == list:
            arr = []
            for r in resp:
                arr.append(obj(**r))
            return arr
        else:
            return obj(**resp)

    # margin
    def get_margin_accounts(self, symbol: str = '') -> typing.Union[typing.List[AccountResponse], AccountResponse]:
        '''
        Get margin accounts
        '''
        return self._get_object_data(self._endpoints['margin'], AccountResponse, symbol)

    # spot
    def get_spot_accounts(self, symbol: str = '') -> typing.Union[typing.List[SpotResponse], SpotResponse]:
        '''
        Get spot accounts
        '''
        return self._get_object_data(self._endpoints['spot'], SpotResponse, symbol)

    # position   
    def get_positions(self, symbol: str = '') -> typing.Union[typing.List[PositionResponse], PositionResponse]:
        '''
        Get Positions
        '''
        return self._get_object_data(self._endpoints['position'], PositionResponse, symbol)
