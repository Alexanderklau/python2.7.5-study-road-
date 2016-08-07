def checkIndex(key):
    if not isinstance(key,(int,long)):raise  TypeError
    if key<0:raise IndexError

class AritmeticSquence:
    def __init__(self,start = 0,step = 1):
        self.start = start
        self.step = step
        self.change = {}
    def __getitem__(self, key):
        checkIndex(key)
        try:return self.change[key]
        except KeyError:
            return self.start + key*self.step
    def __setitem__(self, key, value):
        checkIndex(key)
        self.change[key] = value
