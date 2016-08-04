class Class:
    def method(self):
        print 'I have a self!'
def fuction():
    print "I don't......"
class Bird:
    song = 'Sqaawk!'
    def sing(self):
        print self.song
class Secretive:
    def __inaccessible(self):
        print "Bet you can't see me......"
    def accessible(self):
        print "The secret message is:"
        self.__inaccessible()
class memberCounter:
    members = 0
    def init(self):
        memberCounter.members += 1

