import colander
from bullish.schema.base import DateSchema, IntSchema


class ExchangeTimeSchema(colander.MappingSchema):
    # number of milliseconds since EPOCH as string
    timestamp = IntSchema()
    # ISO 8601 with millisecond as string
    datetime = DateSchema()


class NonceSchema(colander.MappingSchema):
    # lower bound of nonce range
    lowerBound = IntSchema()
    # upper bound of nonce range
    upperBound = IntSchema()
