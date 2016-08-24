import os
for tmpdir in ('/tmp',r'c: \temp'):
    if os.path.isdir(tmpdir):
        break
    else:
        print 'No temp directory avaliable'
        tmpdir = ''
    if tmpdir:
        os.chdir(tmpdir)
        cwd = os.getcwd()
        print '*** current temporary directory'
        print cwd
