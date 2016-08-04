datebase = [
    ['Albert', '1234'],
    ['dilbert','4242'],
    ['Smith',  '7523'],
    ['Jones',  '9843']
]
username = raw_input('User name:')
pin = raw_input('PIN code:')

if [username,pin] in datebase:print 'Access!!!'
