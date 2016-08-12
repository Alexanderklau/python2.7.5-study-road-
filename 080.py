from urllib import urlretrieve
def firstNoBlank(lines):
    for eachLine in lines:
        if not eachLine.strip():
            continue
        else:
            return eachLine
def firstlast(webpage):
    f = open(webpage)
    lines = f.readlines()
    f.close()
    print firstNoBlank(lines),
    lines.reverse()
    print firstNoBlank(lines),
def download(url = 'http://www',process=firstlast):
    try:
        retval = urlretrieve(url)[0]
    except IOError:
        revtal = None
        if retval:
            process(retval)
            if __name__=='__main__':
                download()

