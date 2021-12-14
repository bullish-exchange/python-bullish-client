import colander

from bullish.schema.base import BoolSchema, DateSchema, IntSchema, OrderTypeSchema, SideTypeSchema, StringSchema


class OrderTypeSeqSchema(colander.SequenceSchema):
    orderTypes = OrderTypeSchema()


class MarketSchema(colander.MappingSchema):
    # market ID
    marketId = StringSchema()
    # market symbol
    symbol = StringSchema()
    # base asset symbol
    baseSymbol = StringSchema()
    # quote asset symbol
    quoteSymbol = StringSchema()
    # quote asset id
    quoteAssetId = StringSchema()
    # base asset id
    baseAssetId = StringSchema()
    # quote precision
    quotePrecision = IntSchema()
    # base precision
    basePrecision = IntSchema()
    # number of decimal digits 'after the dot' for price
    pricePrecision = IntSchema()
    # number of decimal digits 'after the dot' for quantity
    quantityPrecision = IntSchema()
    # number of decimal digits 'after the dot' for cost, price * quantity
    costPrecision = IntSchema()
    # order quantity should be > min
    minQuantityLimit = StringSchema()
    # order quantity should be < max
    maxQuantityLimit = StringSchema()
    # order price should be < max
    maxPriceLimit = StringSchema()
    # order price should be > min
    minPriceLimit = StringSchema()
    # order cost, price * quantity should be < max
    maxCostLimit = StringSchema()
    # order cost, price * quantity should be > min
    minCostLimit = StringSchema()
    # time zone
    timeZone = StringSchema()
    # tick size
    tickSize = StringSchema()
    # maker fee in bps
    makerFee = IntSchema()
    # taker fee in bps
    takerFee = IntSchema()
    # [enum]Allowed: LMT|MKT|STOPLIMIT|STOPLOSS
    orderTypes = OrderTypeSeqSchema()
    # spot trading enabled
    spotTradingEnabled = BoolSchema()
    # margin trading enabled
    marginTradingEnabled = BoolSchema()
    # market enabled
    marketEnabled = BoolSchema()


class MarketCandleSchema(colander.MappingSchema):
    # monetary value with 50 decimal place accuracy as string
    open = StringSchema()
    # monetary value with 50 decimal place accuracy as string
    high = StringSchema()
    # monetary value with 50 decimal place accuracy as string
    low = StringSchema()
    # monetary value with 50 decimal place accuracy as string
    close = StringSchema()
    # monetary value with 50 decimal place accuracy as string
    volume = StringSchema()
    # number of milliseconds since EPOCH as string
    createdAtTimestamp = IntSchema()
    # ISO 8601 with millisecond as string
    createdAtDatetime = DateSchema


class BidAskSchema(colander.MappingSchema):
    # monetary value with 50 decimal place accuracy as string
    price = StringSchema()
    # monetary value with 50 decimal place accuracy as string
    priceLevelQuantity = StringSchema()


class BidAskSeqSchema(colander.SequenceSchema):
    bid_ask = BidAskSchema()


class MarketOrderBookSchema(colander.MappingSchema):
    # bids
    bids = BidAskSeqSchema()
    # asks
    asks = BidAskSeqSchema()
    # datetime of orderbook snapshot
    datetime = DateSchema()
    # timestamp of orderbook snapshot
    timestamp = IntSchema()
    # an increasing unique identifier of the orderbook snapshot
    sequenceNumber = IntSchema()


class MarketTickSchema(colander.MappingSchema):
    # denotes the time of the current tick on the exchange
    createdAtDatetime = DateSchema()
    # denotes the time of the current tick on the exchange
    createdAtTimestamp = IntSchema()
    # highest price
    high = StringSchema()
    # lowest price
    low = StringSchema()
    # current best bid (buy) price
    bestBid = StringSchema()
    # current best bid (buy) quantity (may be missing or undefined)
    bidVolume = StringSchema()
    # current best ask (sell) price
    bestAsk = StringSchema()
    # current best ask (sell) quantity (may be missing or undefined)
    askVolume = StringSchema()
    # volume weighed average price
    vwap = StringSchema()
    # opening price
    open = StringSchema()
    # price of last trade (closing price for current period)
    close = StringSchema()
    # price of last trade (closing price for current period)
    last = StringSchema()
    # absolute change, last - open
    change = StringSchema()
    # relative change, (change/open) * 100
    percentage = StringSchema()
    # average price, (last + open) / 2
    average = StringSchema()
    # volume of base asset traded for last 24 hours
    baseVolume = StringSchema()
    # volume of quote asset traded for last 24 hours
    quoteVolume = StringSchema()
    # current price
    bancorPrice = StringSchema()
    # time of the last trade on this symbol
    lastTradeDatetime = DateSchema(missing=None, default=None)
    # time of the last trade on this symbol
    lastTradeTimestamp = IntSchema(missing=None, default=None)
    # quantity of the last trade on this symbol
    lastTradeQuantity = StringSchema()


class MarketTradeSchema(colander.MappingSchema):
    # market symbol
    symbol = StringSchema()
    # price
    price = StringSchema()
    # quantity
    quantity = StringSchema()
    # order side Allowed: BUY|SELL
    side = SideTypeSchema()
    # Allowed: LMT|MKT|STOP_LIMIT order type
    type = OrderTypeSchema()
    # denotes the time the trade was executed by the exchange
    createdAtDatetime = DateSchema()
    # denotes the time the trade was executed by the exchange
    createdAtTimestamp = IntSchema()
