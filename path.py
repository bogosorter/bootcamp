def path():
    raise NotImplementedError

def read(filename):
    with open(filename) as f:
        return [[int(i) for i in line.split()] for line in f.readlines()]
