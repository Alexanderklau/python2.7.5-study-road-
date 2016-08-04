filename = raw_input('Enter file name:')
f = open(filename,'r')
allLines = f.readlines()
f.close()
for eachLine in allLines:
    print eachLine