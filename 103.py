filename = raw_input('Enter file name')
f = open(filename,'w')
for eachLine in f:
    print eachLine,
f.close()