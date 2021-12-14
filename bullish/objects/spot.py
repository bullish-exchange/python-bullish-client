from bullish.schema.spot import  SpotSchema
from bullish.objects.base import Base


class  SpotResponse(Base):
    def __init__(self, **kwargs):
        super( SpotResponse, self).__init__( SpotSchema(), kwargs)
    # TODO add __str__
    # TODO add __repr__
