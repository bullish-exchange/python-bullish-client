from bullish.objects.paging import PageLink
from bullish.schema.trade import TradePageSchmea, TradeResponseSchema
from bullish.objects.base import Base


class TradeResponse(Base):
    def __init__(self, **kwargs):
        super(TradeResponse, self).__init__(TradeResponseSchema(), kwargs)
    # TODO add __str__
    # TODO add __repr__

    # TODO is this needed?
    def to_dict(self):
        '''
        output a dict
        '''
        return self.__dict__


class TradePageResponse(Base):
    def __init__(self, **kwargs):
        super(TradePageResponse, self).__init__(TradePageSchmea(), kwargs)
        # TODO is there a better way?
        cnt = 0
        while cnt < len(self.data):
            self.data[cnt] = TradeResponse(**self.data[cnt])
            cnt += 1
        # process links
        self.links = PageLink(**self.links)