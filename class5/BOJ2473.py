# pypy

import sys


def search(a, b):
    tmp = numbers[a] + numbers[b]
    start, end = b+1, N-1

    result = sys.maxsize
    return_value = sys.maxsize
    while start <= end:
        center = (start+end) // 2
        calculate = tmp + numbers[center]
        if abs(calculate) < abs(result):
            result = abs(calculate)
            return_value = numbers[center]
        if calculate > 0:
            end = center - 1
        elif calculate < 0:
            start = center + 1
        else:
            print(numbers[a], numbers[b], numbers[center])
            exit()
    return (result, return_value)


sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
numbers = sorted(list(map(int, input().split())))
result = sys.maxsize
answer = (-1, -1, -1)
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        val, ans = search(i, j)
        if val < result:
            answer = (numbers[i], numbers[j], ans)
            result = val
print(*answer)
