people = {
    'Alice':{
        'Phone':'2341',
        'addr':'foo dive 23'
    },
    'Beth':{
        'Phone':'9102',
        'addr':'Bar street 42'
    },
    'Cecil':{
        'Phone':'3158',
        'addr':'Baz avenue 90'
    }
}

labels = {
    'Phone':'Phone number',
    'addr':'address'
}
name = raw_input('name:')
request = raw_input('Phone number (p) or address (a)?')
if request == 'p':key = 'Phone'
if request == 'a':key = 'addr'
if name in people :print "%s's %s is %s."% \
                         (name,labels[key],people[name][key])