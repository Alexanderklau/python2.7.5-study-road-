people = {
    'aplice': {
        'phone':'2341',
        'addr':'foo drive 23'
    },
    'beth': {
        'phone':'9102',
        'addr':'bar street 42'
    },
    'caci': {
        'phone':'3158',
        'adde':'baz aven 90'
    }
}
labels = {
    'phone':'phone number',
    'addr':'address'
}
name = raw_input('name: ')
request = raw_input('phone number (p) or address (a)?')
if request == 'p':key  ='phone'
if request == 'a':key = 'addr'
if name in people :print  "%s' s %s is %s." %\
    (name ,labels[key],people[name][key])