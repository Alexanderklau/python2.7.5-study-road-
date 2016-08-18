CODEC = 'utf-8'
FILE = 'lwb.txt'

hello_out = u'Hello world\n' \
            u'i wanna go to school\n'
bytes_out = hello_out.encode(CODEC)
f = open(FILE,'w')
f.write(bytes_out)
f.close()

f = open(FILE,"r")
bytes_in = f.read()
f.close()
hello_in = bytes_in.decode(CODEC)
print hello_in,

