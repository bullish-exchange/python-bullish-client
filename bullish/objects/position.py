from bullish.schema.position import PositionSchema
from bullish.objects.base import Base


class PositionResponse(Base):
    def __init__(self, **kwargs):
        super(PositionResponse, self).__init__(PositionSchema(), kwargs)
    # TODO add __str__
    # TODO add __repr__
