people = {
    'lwb':{
        'Phone':'1234',
        'addr':'lwb street'
    },
    'Stevie':{
        'Phone':'2212',
        'addr':'attacked'
    }

}

labels = {
    'Phone':'phone number',
    'addr':'address'
}
name = raw_input('Name:')
request = raw_input('Phone number(p)or address (a)?')

if request == 'p':key = 'Phone'
if request == 'a':key = 'addr'
#if name in people:print "%s's %s is %s." %(name,labels[key],people[name][key])
person = people.get(name,{})
labe = labels.get(key,key)
result = person.get(key,'not available')
print "%s's %s is %s" %(name,labe,result)
