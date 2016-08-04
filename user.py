database = [
    ['albert', '1234'],
    ['dlibert','4242'],
    ['lwb',    '1368'],
    ['jones',  '9843'],
]
username = raw_input('user name:')
pin = raw_input('PIN Code')
if [username,pin] in database:print 'Access granted'