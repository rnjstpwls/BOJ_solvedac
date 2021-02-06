import sys
from collections import deque

input = sys.stdin.readline

X = int(input())

q = deque()
q.append((X, 0))
visited = [False] * X
while q:
    num, cnt = q.popleft()
    if num == 1:
        print(cnt)
        break

    if num % 3 == 0 and not visited[num // 3]:
        visited[num // 3] = True
        q.append((num // 3, cnt+1))

    if num % 2 == 0 and not visited[num // 2]:
        visited[num // 2] = True
        q.append((num // 2, cnt+1))
    if not visited[num-1]:
        visited[num-1] = True
        q.append((num-1, cnt+1))