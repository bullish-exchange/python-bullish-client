import colander
from bullish.schema.base import StringSchema

class AccountResponseSchema(colander.MappingSchema):
    # margin account ID
    accountId = StringSchema()
    # symbol
    symbol = StringSchema()
    # base free
    baseFree = StringSchema()
    # quote free
    quoteFree = StringSchema()
    # base used
    baseUsed = StringSchema()
    # quote used
    quoteUsed = StringSchema()
    # base total
    baseTotal = StringSchema()
    # quote total
    quoteTotal = StringSchema()
    # base debt
    baseDebt = StringSchema()
    # quote debt
    quoteDebt = StringSchema()
    # base call price
    baseCallPrice = StringSchema()
    # quote call price
    quoteCallPrice = StringSchema()
    # base principal
    basePrincipal = StringSchema()
    # quote principa\
    quotePrincipal = StringSchema()