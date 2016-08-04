class Filter:
    def __init__(self):
        self.blocked = []
    def filter(self,sequence):
        return [x for x in  sequence if x not in self.blocked]
class SPAMFilter(Filter):
    def __init__(self):
        self.blocked = ['SPAM']