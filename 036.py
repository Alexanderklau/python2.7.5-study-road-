def lines(file):
    for line in file:yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
