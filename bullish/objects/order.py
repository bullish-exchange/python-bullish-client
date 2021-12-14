from bullish.objects.base import Base
from bullish.objects.paging import PageLink
from bullish.schema.order import OrderCreateSchema, OrderCancelSchema, OrderResponseSchema, OrderResultSchema, OrderPageResponseSchema


class OrderCreate(Base):
    def __init__(self, **kwargs):
        super(OrderCreate, self).__init__(OrderCreateSchema(), kwargs)
    # TODO add __str__
    # TODO add __repr__

    def to_dict(self):
        '''
        output a dict in the order expected by the Bullish API
        '''
        return {
            'commandType': self.commandType,
            'handle': self.handle,
            'symbol': self.symbol,
            'type': self.type,
            'side': self.side,
            'price': self.price,
            'stopPrice': self.stopPrice,
            'quantity': self.quantity,
            'timeInForce': self.timeInForce,
            'allowMargin': self.allowMargin
        }


class OrderResult(Base):
    def __init__(self, **kwargs):
        super(OrderResult, self).__init__(OrderResultSchema(), kwargs)
    # TODO add __str__
    # TODO add __repr__


class OrderResponse(Base):
    def __init__(self, **kwargs):
        super(OrderResponse, self).__init__(OrderResponseSchema(), kwargs)

class OrderCancel(Base):
    def __init__(self, **kwargs):
        super(OrderCancel, self).__init__(OrderCancelSchema(), kwargs)

    def to_dict(self):
        '''
        output a dict in the order expected by the Bullish API
        '''
        return {
            'commandType': self.commandType,
            'orderId': self.orderId,
            'handle': self.handle,
            'symbol': self.symbol
        }


class OrderPageResponse(Base):
    def __init__(self, **kwargs):
        super(OrderPageResponse, self).__init__(OrderPageResponseSchema(), kwargs)
        # process orders
        # TODO is there a better way?
        cnt = 0
        while cnt < len(self.data):
            self.data[cnt] = OrderResult(**self.data[cnt])
            cnt += 1
        # process links
        self.links = PageLink(**self.links)
