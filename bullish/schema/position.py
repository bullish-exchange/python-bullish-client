from bullish.schema.base import DateSchema, IntSchema, StringSchema
import colander

class RiskSchema(StringSchema):
    validator = colander.OneOf(['LOW', 'MEDIUM', 'HIGH'])


class PositionTypeSchema(StringSchema):
    validator = colander.OneOf(['LONG', 'SHORT'])


class PositionSchema(colander.MappingSchema):
    # position ID
    positionId = StringSchema()
    # symbol
    symbol = StringSchema()
    # leverage
    leverage = StringSchema()
    # leverage
    maxLeverage = StringSchema()
    # leverage
    utilisation = StringSchema()
    # quantity
    quantity = StringSchema()
    # base loan amount
    baseLoanAmount = StringSchema()
    # quote loan amount
    quoteLoanAmount = StringSchema()
    # daily interest rate percentage
    dailyInterestRatePercentage = StringSchema()
    # base accrued interest amount
    baseAccruedInterestAmount = StringSchema()
    # quote accrued interest amount
    quoteAccruedInterestAmount = StringSchema()
    # liquidation risk Allowed: LOW┃MEDIUM┃HIGH
    liquidationRisk = RiskSchema()
    # liquidation price
    liquidationPrice = StringSchema()
    # long vs short Allowed: LONG┃SHORT
    positionType = PositionTypeSchema() 
    # The time the position was retrieved
    updatedAtDatetime = DateSchema()
    # The time the position was
    updatedAtTimestamp = IntSchema()