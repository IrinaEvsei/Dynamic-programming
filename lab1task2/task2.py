def find_IS(arr):
    d, path = list(), list()

    path.extend([0, int(arr[0] <= arr[1])])
    d.extend([0, arr[0], max(arr[0], arr[1])])

    for i in range(2, len(arr)):
        d.append(max(d[i - 1] + arr[i], d[i]))

        if d[i - 1] + arr[i] > d[i]:
            path.append(i)

    for i in range(len(path) - 1, 0, -1):
        if path[i] - path[i - 1] < 2:
            path.pop(i - 1)
    return path


if __name__ == '__main__':
    with open('task2.txt', 'r') as f:
        numbers = []
        for line in f:
            numbers.extend(list(map(int, line.split())))
    path = find_IS(numbers)
    for i in path:
        print(f'{numbers[i]}({i+1})', end=' ')
