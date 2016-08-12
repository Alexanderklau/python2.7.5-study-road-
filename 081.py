def dictVarArgs(arg1,arg2='defaultB',**theRest):
    'display 2 regular args and keyword variable args'
    print 'Form arg1:',arg1
    print 'Form arg2:',arg2
    for eachXtrArg in theRest.keys():
        print 'Xtra arg %s: %s' % (eachXtrArg,str(theRest[eachXtrArg]))
