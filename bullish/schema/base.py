from datetime import datetime
import colander


class BaseSchema(colander.SchemaNode):
    required = True


class StringSchema(BaseSchema):
    schema_type = colander.String
    missing = None
    default = ''


class BoolSchema(BaseSchema):
    schema_type = colander.Bool


class IntSchema(BaseSchema):
    schema_type = colander.Int


class DateSchema(BaseSchema):
    schema_type = colander.DateTime
    
    def preparer(self, appstruct):
        if type(appstruct) == datetime:
            return appstruct.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
        else:
            return appstruct


class OrderTypeSchema(StringSchema):
    validator = colander.OneOf(['LMT', 'MKT', 'STOPLIMIT', 'STOPLOSS'])


class SideTypeSchema(StringSchema):
    validator = colander.OneOf(['BUY', 'SELL'])


class TimeInForceSchema(StringSchema):
    validator = colander.OneOf(['FOK', 'GTC', 'IOC'])


class OrderStatusSchema(StringSchema):
    validator = colander.OneOf(['OPEN', 'CLOSED', 'CANCELLED', 'REJECTED'])
