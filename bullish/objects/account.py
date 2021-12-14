from bullish.schema.account import AccountResponseSchema
from bullish.objects.base import Base


class AccountResponse(Base):
    def __init__(self, **kwargs):
        super(AccountResponse, self).__init__(AccountResponseSchema(), kwargs)
    # TODO add __str__
    # TODO add __repr__
