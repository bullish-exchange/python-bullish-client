from bullish.schema.market import BidAskSchema, MarketSchema, MarketCandleSchema, MarketOrderBookSchema, MarketTickSchema, MarketTradeSchema
from bullish.objects.base import Base


class Market(Base):
    def __init__(self, d: dict):
        super(Market, self).__init__(MarketSchema(), d)
    
    def __str__(self) -> str:
        return f'{self.marketId} {self.symbol}'


class MarketCandle(Base):
    def __init__(self, d: dict):
        super(MarketCandle, self).__init__(MarketCandleSchema(), d)


class MarketBidAsk(Base):
    def __init__(self, d: dict):
        super(MarketBidAsk, self).__init__(BidAskSchema(), d)


class MarketOrderBook(Base):
    def __init__(self, d: dict):
        super(MarketOrderBook, self).__init__(MarketOrderBookSchema(), d)
        self._convert_bids_asks(self.bids)
        self._convert_bids_asks(self.asks)

    def _convert_bids_asks(self, convert: dict):
        cnt = 0
        while cnt < len(convert):
            convert[cnt] = MarketBidAsk(convert[cnt])
            cnt = cnt + 1


class MarketTick(Base):
    def __init__(self, d: dict):
        super(MarketTick, self).__init__(MarketTickSchema(), d)


class MarketTrade(Base):
    def __init__(self, d: dict):
        super(MarketTrade, self).__init__(MarketTradeSchema(), d)
