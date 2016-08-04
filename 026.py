class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def next(self):
        self.a,self.b,self.a + self.b
        return self.a
    def __iter__(self):
        return self
class TestIterator:
    value = 0
    def next(self):
        self.value += 1
        if self.value > 10: raise  StopIteration
        return self.value
    def __iter__(self):
        return self