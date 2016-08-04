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
key = request
if request == 'p':key = 'Phone'
if request == 'a':key = 'addr'
person = people.get(name,{})
label = labels.get(key,key)
result = person.get(key,'not avaliable')
print "%s's %s is %s."% (name,label,result)
