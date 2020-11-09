import sys


def search(idx, selected):
    if len(selected) > M:
        return
    if idx == N:
        if len(selected) == M:
            print(*selected)
        return
    search(idx+1, selected+[numbers[idx]])
    search(idx+1, selected)


input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(range(1, N+1))
search(0, [])