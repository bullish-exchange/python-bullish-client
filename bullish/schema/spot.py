from bullish.schema.base import DateSchema, IntSchema, StringSchema
import colander

class SpotSchema(colander.MappingSchema):
    # spot account ID
    accountId = StringSchema()
    # asset symbol
    currency = StringSchema()
    # asset symbol
    symbol = StringSchema()
    # total, free + used
    total = StringSchema()
    # money available for trading
    free = StringSchema()
    # money on hold, locked, frozen
    used = StringSchema()