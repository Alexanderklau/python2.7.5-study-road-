def safe_float(obj):
    'safe version of float()'
    try:
        retval = float(obj)
    except (ValueError,TypeError),diag:
        retval = str(diag)
        return  retval
def main():
    'handles all the data processing'
    log = open('AlexCard.txt','w')
    try:
        ccfile = open('data.txt','r')
    except IOError, e:
        log.write('Mp txns this month\n')
        log.close()
        return
    txns = ccfile.readlines()
    ccfile.close()
    total = 0.00
    log.write('account log:\n')

    for eachTxn in txns:
        result = safe_float(eachTxn)
        if isinstance(result,float):
            total += result
            log.write('data.....processed\n')
        else:
            log.write('ignored: %s ' % result)
    print '$%.2f (nes balance)' % (total)
    log.close()
if __name__=='__main__':
    main()
