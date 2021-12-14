import colander
from bullish.schema.base import DateSchema, IntSchema, SideTypeSchema, StringSchema
from bullish.schema.paging import PageLinksSchema


class TradeResponseSchema(colander.MappingSchema):
    # trade ID
    tradeId = StringSchema()
    # order ID
    orderId = StringSchema()
    # market symbol
    symbol = StringSchema()
    # price
    price = StringSchema()
    # quantity
    quantity = StringSchema()
    # base fee
    baseFee = StringSchema()
    # quote fee
    quoteFee = StringSchema()
    # order side Allowed: BUY┃SELL
    side = SideTypeSchema()
    # denotes the time the trade was executed by the exchange
    createdAtDatetime = DateSchema()
    # denotes the time the trade was executed by the exchange
    createdAtTimestamp = IntSchema()

class TradeDataSchema(colander.SequenceSchema):
    data = TradeResponseSchema()


class TradePageSchmea(colander.MappingSchema):
    data = TradeDataSchema()
    links = PageLinksSchema()