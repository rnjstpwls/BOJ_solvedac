import sys


def search(idx, shop):
    global result
    if idx == len(bbq):
        if len(shop) == M:
            result = min(order(shop), result)
        return

    if len(shop) > M:
        return

    search(idx + 1, shop)
    search(idx + 1, shop + [bbq[idx]])


def length(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def order(shop):
    total = 0
    for h in home:
        tmp = float('inf')
        for s in shop:
            tmp = min(length(h, s), tmp)
        total += tmp
    return total


sys.stdin = open('input.txt')

input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(list(map(int, input().split())) for _ in range(N))

home = []
bbq = []

for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:
            home.append((r, c))
        elif arr[r][c] == 2:
            bbq.append((r, c))
result = float('inf')
search(0, [])
print(result)
