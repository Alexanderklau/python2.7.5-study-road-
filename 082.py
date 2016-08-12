def testir(func,*nkwargs,**kwargs):
    try:
        retval = func(*nkwargs,**nkwargs)
        result = (True,retval)
    except Exception,diag:
        result = (False,str(diag))
    return result
def test():
    funcs = (int,long,float)
    vals = (1234,12.32,'1234','123.2')
    for eachFunc in funcs:
        print '_' * 20
        for eachVal in vals:
            retval = testir(eachFunc,eachVal)
            if retval[0]:
                print '%S(%S) = ' % (eachFunc.__name__,'eachVal'),retval[1]
            else:
                print '%S(%S) = FAILED:'%(eachFunc.__name__,'eachVal'),retval[1]
    if __name__=='__main__':
        test()
