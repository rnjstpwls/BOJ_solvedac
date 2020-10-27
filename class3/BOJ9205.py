import sys
from collections import deque


def length(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    sanggeun = tuple(map(int, sys.stdin.readline().split()))
    CU = list(tuple(map(int, sys.stdin.readline().split())) for _ in range(N+1))
    festival = CU[-1]

    if length(sanggeun, festival) <= 1000:
        print('happy')
        continue

    q = deque([sanggeun])
    visited = {sanggeun}
    result = 'sad'

    while q:
        current = q.popleft()
        if current == festival:
            result = 'happy'
        for conv in CU:
            if length(current, conv) <= 1000 and conv not in visited:
                q.append(conv)
                visited.add(conv)
    print(result)