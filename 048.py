class Calculator:
    def calculator(self,expression):
        self.value = eval(expression)

class Talker:
    def talk(self):
        print 'Hi,my value is',self.value
class TalkingCalculator(Calculator,Talker):
    pass