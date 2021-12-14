from bullish import Bullish
from bullish.objects.order import OrderCreate, OrderCancel

import datetime as dt

import config

if __name__ == '__main__':

    conn = Bullish(config.hostname, config.email, config.api_key_priv)

    # get challenge and generate
    conn.session_init()

    # get exchange time
    print(conn.get_exchange_time().__dict__)
    print(conn.get_nonce().__dict__)

    # get markets
    markets = conn.get_markets()
    print(f'Found {len(markets)} markets')
    for m in markets:
        print(m.symbol)

    market = conn.get_market('ETHBTC')
    print(market.__dict__)
    print(
        f'maxPriceLimit: {market.maxPriceLimit} minPriceLimit: {market.minPriceLimit}')

    # get market candle
    endTs = dt.datetime.utcnow()
    startTs = dt.datetime.utcnow() - dt.timedelta(hours=80)
    candles = conn.get_market_candle(
        'ETHBTC', startTime=startTs, endTime=endTs, timeBucket='30m')
    if len(candles) > 0:
        print('get_market_candle')
        print(candles[0].__dict__)

    # get orders
    print('get_market_orderbook')
    orders = conn.get_market_orderbook('ETHBTC')
    print(orders.bids[0].__dict__)

    # get tick
    print('get_market_tick')
    tick = conn.get_market_tick('ETHBTC')
    print(tick.__dict__)

    # get trade
    print('get_market_trade')
    trade = conn.get_market_trade('ETHBTC')
    if len(trade) > 0:
        print(trade[0].__dict__)
    else:
        print('No market trades found')

    # ORDERS
    print('create_order')
    new_ord = OrderCreate(handle=None,
                          symbol="BTCUSD",
                          type="LMT",
                          side="BUY",
                          price="1000.0",
                          quantity="2.0",
                          timeInForce="GTC"
                          )

    created_order = conn.create_order(new_ord)
    print(created_order.__dict__)

    # get order by id
    print('get_orders_by_id')
    ord = conn.get_order_by_id(created_order.orderId)
    print(ord.__dict__)

    # get order
    print('get_orders')
    orders = conn.get_orders(symbol='BTCUSD')
    print(orders[0].__dict__)

    # get order
    print('get_orders:OPEN:BUY')
    orders = conn.get_orders(symbol='BTCUSD', side='BUY', status='OPEN')

    print(orders[0].__dict__)

    # delete order
    print('delete_order')
    del_ord = OrderCancel(orderId=ord.orderId,
                          handle=ord.handle, symbol=ord.symbol)
    deleted = conn.cancel_order(del_ord)
    print(deleted.__dict__)

    # trades
    print('get_trades')
    tradeId = 0
    trades = conn.get_trades()
    if len(trades) > 0:
        tradeId = trades[0].tradeId
        print(trades[0].__dict__)

    if tradeId:
        print('get_trade_by_id')
        tr = conn.get_trade_by_id(tradeId)
        print(tr.__dict__)

    # margin accounts
    print('get_margin_accounts')
    accts = conn.get_margin_accounts()
    if len(accts) > 0:
        print(accts[0].__dict__)

    print('get_margin_accounts::BTCUSD')
    acct = conn.get_margin_accounts('BTCUSD')
    print(acct.__dict__)

    # spot accounts
    print('get_spot_account')
    spots = conn.get_spot_accounts()
    if len(spots) > 0:
        print(spots[0].__dict__)

    print('get_spot_account::BTC')
    spot = conn.get_spot_accounts('BTC')
    print(spot.__dict__)