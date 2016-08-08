def conflict(state,nextX):#定义一个新的函数confice
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0,nextY - i):
            return True
    return False
def queens(num=8,state=()):
    for pos in range(num):
        if not  conflict(state,pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num,state + (pos,)):
                    yield (pos,) + result
def prettypring(soulution):
    def line(pos,length = len(soulution)):
        return '. ' * (pos) + 'X' + '. ' *(length-pos-1)
    for pos in soulution:
        print line(pos)

