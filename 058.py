_metaclass_=type
class MyClass:
    def smeth():
        print 'This is a staic method'
    smeth = staticmethod(smeth)
    def cmeth(cls):
        print 'This is a class method of',cls
    cmeth = classmethod(cmeth)
