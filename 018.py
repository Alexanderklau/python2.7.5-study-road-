class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print 'Aaaaaah.....'
            self.hungry = False
        else:
            print 'No,thanks!'
class Song(Bird):
    def __init__(self):
        super(Song,self).__init__()
        self.sound = 'Squawk!'
    def sing(self):
        print self.sound
