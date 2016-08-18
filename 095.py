import string

alphas = string.letters + '_'
nums = string.digits
print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long.'
myInput = raw_input('Identifier to test? ')
if len(myInput) > 1:
    if myInput[0] not in alphas:
        print '''invalid:first symbol must be alphbetic'''#检查第一个符号是不是字母或者下划线
    else:
        for otherChar in myInput[1:]:             #从第二的字符开始循环查找
            if otherChar not in alphas + nums:
                print '''invalid:remaining symbols must be alphanumeric'''
                break
            else:
                print "okay as an identifier"

