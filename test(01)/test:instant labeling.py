def lines(file):
    for line in file:yield
    yield ' \n '
def blocks(file):
    block = []
    for line in lines:
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []
