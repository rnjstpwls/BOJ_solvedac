# pypy

import sys
N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(trees)

while start <= end:
    total = 0
    mid = (start+end)//2
    for t in trees:
        if t > mid:
            total += (t-mid)

    if total >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)