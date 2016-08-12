def covert (func,seq):
    'conv. sequence of numbers to same type'
    return [func(eachNum)for eachNum in seq]

myseq = (123,34,21,-2,2e8,9999999999L)
print covert(int,myseq)
print covert(long,myseq)
print covert(float,myseq)
