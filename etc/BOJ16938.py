import sys

def search(idx, minv, maxv, sumv, cnt):
    global result
    if R < sumv:
        return
    if idx == N:
        if cnt >= 2 and L <= sumv <= R and maxv - minv >= X:
            result += 1
        return
    search(idx+1, minv, maxv, sumv, cnt)
    tmp_min = min(minv, arr[idx])
    tmp_max = max(maxv, arr[idx])
    search(idx+1, tmp_min, tmp_max, sumv+arr[idx], cnt+1)
    pass


sys.stdin = open('input.txt')

input = sys.stdin.readline

N, L, R, X = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = 0
search(0, sys.maxsize, -sys.maxsize, 0, 0)
print(result)