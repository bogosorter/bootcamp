def sudoku():
    raise NotImplementedError

def read():
    with open('sudoku.txt') as f:
        result = []
        current = []
        for line in f.readlines()[1:]:
            if line[0] == 'G': result.append(current)
            else: current.append([int(c) for c in line if c != '\n'])
        result.append(current)
    return result

