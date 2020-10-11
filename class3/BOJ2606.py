import sys
from collections import deque

N = int(sys.stdin.readline())
link = [[] for _ in range(1+N)]

for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    link[a].append(b)
    link[b].append(a)

q = deque([1])
visited = set()
visited.add(1)
while q:
    current = q.popleft()

    for element in link[current]:
        if element in visited:
            continue
        else:
            q.append(element)
            visited.add(element)
print(len(visited)-1)
