import end as end


def inputD():
    data = []
    with open("task1.txt") as f:
        for line in f:
            data.append(list(map(int, line.split())))
    k, x, r = data
    for i in k:
        m = i
    return m, x, r


def find_opt(n, x, r):
    opt, path = list(), list()

    path.append(0)
    opt.extend([0, r[0]])

    for i in range(1, n):
        index = get_opt_point(x, i)
        opt.append(max(r[i] + opt[index], opt[i]))

        if r[i] + opt[index] > opt[i]:
            path.append(i)

    printPath(path, x)


def get_opt_point(x, i):
    index = 0
    while x[i] - x[index] > 5:
        index += 1

    return index


def printPath(path, x):
    for i in range(len(path) - 1, 1, -1):
        if x[path[i]] - x[path[i - 1]] < 6:
            path.pop(i - 1)

    for i in path:
        print(x[i], end=' ')


if __name__ == '__main__':
    find_opt(*inputD())
