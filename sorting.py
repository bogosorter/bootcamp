def sort(ls):
    raise NotImplementedError

tests = [
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [],
    [4, 3, 5, 1, 2],
    [3, 7, 2],
    [-3, -2, -5, 8]
]
results = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [],
    [1, 2, 3, 4, 5],
    [2, 3, 7],
    [-5, -3, -2, 8]
]

for i, (test, result) in enumerate(zip(tests, results)):
    if sort(test) != result:
        print('Wrong Answer')
        quit()
print('Accepted')