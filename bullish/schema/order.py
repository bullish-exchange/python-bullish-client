import colander
from bullish.schema.base import BoolSchema, DateSchema, IntSchema, OrderStatusSchema, OrderTypeSchema, SideTypeSchema, StringSchema, TimeInForceSchema
from bullish.schema.paging import PageLinksSchema

class OrderCreateSchema(colander.MappingSchema):
    # commandType
    commandType = StringSchema(missing='V1CreateOrder')
    # order handle
    handle = StringSchema(missing=None, default=None)
    # market symbol
    symbol = StringSchema()
    # order type Allowed: LMT|MKT|STOP_LIMIT
    type = OrderTypeSchema()
    # order side Allowed: BUY|SELL
    side = SideTypeSchema()
    # price
    price = StringSchema()
    # stop price
    stopPrice = StringSchema(missing=None, default=None)
    # quantity
    quantity = StringSchema()
    # time in force Allowed: FOK|GTC|IOC
    timeInForce = TimeInForceSchema()
    # allow margin trading
    allowMargin = BoolSchema(missing=False, default=False)


class OrderResultSchema(colander.MappingSchema):
    # Unique numeric identifier generated on the client side expressed as a string value
    handle = StringSchema()
    # unique order ID
    orderId = StringSchema()
    # market symbol
    symbol = StringSchema()
    # price, see monetary value format
    price = StringSchema()
    # average fill price, see monetary value format
    averageFillPrice = StringSchema()
    # stop price, see monetary value format
    stopPrice = StringSchema()
    # is margin order
    margin = BoolSchema()
    # quantity, see monetary value format
    quantity = StringSchema()
    # quantity filled, see monetary value format
    quantityFilled = StringSchema()
    # base fee, see monetary value format
    baseFee = StringSchema()
    # quote fee, see monetary value format
    quoteFee = StringSchema()
    # order side Allowed: BUY┃SELL
    side = SideTypeSchema()
    # order type  Allowed: LMT┃MKT┃STOP_LIMIT
    type = OrderTypeSchema()
    # time in force Allowed: GTC
    timeInForce = TimeInForceSchema()
    # order status Allowed: OPEN┃CLOSED┃CANCELED┃REJECTED
    status = OrderStatusSchema()
    # status reason, describes why the order is in a specific state
    statusReason = StringSchema()
    # status reason code, is the code associated to the statusReason. This code always stays the same whereas the statusReason might slightly change over time with consequent releases
    statusReasonCode = IntSchema()
    # denotes the time the order was ACK'd by the exchange, ISO 8601 with millisecond as string
    createdAtDatetime = DateSchema()
    # denotes the time the order
    createdAtTimestamp = IntSchema()



class OrderCancelSchema(colander.MappingSchema):
    # command
    command = 'V1CancelOrder'
    commandType = StringSchema(missing=command, default=command)
    # order ID
    orderId = StringSchema()
    # order handle
    handle = StringSchema()
    # symbol
    symbol = StringSchema()


class OrderResponseSchema(colander.MappingSchema):
    # message
    message = StringSchema()
    # unique request Id
    requestId = StringSchema()
    # unique order Id
    orderId = StringSchema()
    # handle
    handle = StringSchema(missing='', default='')
    # test
    test = BoolSchema(missing=False, default=False)


class OrderDataSchema(colander.SequenceSchema):
    data = OrderResultSchema()


class OrderPageResponseSchema(colander.MappingSchema):
    data = OrderDataSchema()
    links = PageLinksSchema()
    