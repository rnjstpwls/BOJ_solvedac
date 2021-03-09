import sys


def search(idx, val):
    global result
    if idx == 11:
        result = max(result, val)
        return

    for i in range(11):
        if arr[idx][i] and not visited[i]:
            visited[i] = True
            search(idx+1, val+arr[idx][i])
            visited[i] = False



sys.stdin = open('input.txt')

input = sys.stdin.readline

C = int(input())

for _ in range(C):
    arr = list(list(map(int, input().split())) for _ in range(11))
    visited = [False] * 11
    result = -1
    for i in range(11):
        if arr[0][i]:
            visited[i] = True
            search(1, arr[0][i])
            visited[i] = False
    print(result)