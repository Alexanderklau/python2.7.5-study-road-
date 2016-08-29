class hotelroomcalc(object):
    'Hotel room rate calculator'
def __init__(self,rt,sales=0.85,rm=0.1):
    '''HotelRoomCalc default arguments:
    sales tax == 8.2% and room tax == 10%'''
    self.saleTax = sales
    self.roomTax = rm
    self.roomRate = rt
def calTotal(self,days=1):
    'Calculate total:default to daily rate'
    daily = round((self.roomRate *
                  (1 + self.roomTax + self.selesTax)),2)
    return float(days) * daily