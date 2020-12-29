import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
visited = [False] * (N + 1)
visited[N] = True
q = deque()
q.append([N])
while q:
    current = q.popleft()
    if current[-1] == 1:
        print(len(current) - 1)
        print(*current)
        break

    if current[-1] % 3 == 0 and not visited[current[-1] // 3]:
        q.append(current + [current[-1] // 3])
        visited[current[-1] // 3] = True
    if current[-1] % 2 == 0 and not visited[current[-1] // 2]:
        q.append(current + [current[-1] // 2])
        visited[current[-1] // 2] = True
    if not visited[current[-1] - 1]:
        q.append(current + [current[-1] - 1])
