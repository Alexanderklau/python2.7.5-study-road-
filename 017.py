class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print 'Ahhhh....'
            self.hungry = False
        else:
            print 'No,Thanks!'
class Song(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.sound = 'squwkkkkk......'
    def sing(self):
        print self.sound
