import sys
from collections import deque


def search(idx):
    q = deque()
    q.append(idx)
    visited = set()

    while q:
        current = q.popleft()
        for i in range(N):
            if arr[current][i] and i not in visited:
                q.append(i)
                visited.add(i)
                result[idx][i] = 1
    pass


N = int(sys.stdin.readline())
arr = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))

result = list([0]*N for _ in range(N))

for i in range(N):
    search(i)

for row in result:
    print(*row)