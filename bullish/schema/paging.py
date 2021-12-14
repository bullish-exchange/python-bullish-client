import colander 
from bullish.schema.base import StringSchema

class PageLinksSchema(colander.MappingSchema):
    next = StringSchema(default=None, missing=None)
    previous = StringSchema(default=None, missing=None)