from bullish.objects.base import Base
from bullish.schema.error import ErrorSchema
from bullish.objects.exception import KeyException, InvalidReqestException, LoginException

class Error(Base):
    def __init__(self, d: dict):
        super(Error, self).__init__(ErrorSchema(), d)
    
    def raise_error(self):
        '''
        '''
        ex_switcher = {
            8008: KeyException(),
            8009: KeyException(),
            8010: InvalidReqestException(),
            8012: LoginException(),
        }
        # get the exception or use default exception
        ex = ex_switcher.get(self.errorCode, Exception(f'{self.errorCodeName}({self.errorCode}): {self.message}'))
        raise ex
