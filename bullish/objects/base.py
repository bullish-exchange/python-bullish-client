from colander import Invalid


class Base(object):

    def __init__(self, validator, d):
        ''' '''
        obj = validator.deserialize(d)
        for k, v in obj.items():
            setattr(self, k, v)
