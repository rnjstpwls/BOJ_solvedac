import sys
from collections import deque


def search(idx):
    q = deque()
    visited = {idx}
    for i in link[idx]:
        q.append((i, 1))
        visited.add(i)
    result = len(q)
    while q:
        current, value = q.popleft()

        for i in link[current]:
            if i in visited:
                continue
            q.append((i, value+1))
            visited.add(i)
            result += (value+1)
    return result


N, M = map(int, sys.stdin.readline().split())
link = [list() for _ in range(1+N)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    link[a].append(b)
    link[b].append(a)
# print(link)
result = []
for i in range(1, N+1):
    result.append(search(i))
print(1 + result.index(min(result)))