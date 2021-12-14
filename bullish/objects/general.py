from bullish.objects.base import Base
from bullish.schema.general import ExchangeTimeSchema, NonceSchema


class ExchangeTime(Base):
    def __init__(self, d: dict):
        super(ExchangeTime, self).__init__(ExchangeTimeSchema(), d)


class Nonce(Base):
    def __init__(self, d: dict):
        super(Nonce, self).__init__(NonceSchema(), d)
