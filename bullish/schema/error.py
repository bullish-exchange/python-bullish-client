from collections import defaultdict
import colander

from bullish.schema.base import IntSchema, StringSchema

class ErrorSchema(colander.MappingSchema):
    message = StringSchema()
    errorCode = IntSchema(missing=-1, default=-1)
    errorCodeName = StringSchema(missing='GenericError', default='GenericError')