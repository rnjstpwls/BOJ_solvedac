import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())

visited = [0] * (N+1)
time = [0] * (N+1)
link = [[] for _ in range(N+1)]
link_aq = [[] for _ in range(N+1)]
q = deque()
cnt = 0
for i in range(1, N+1):
    t, *req, end = map(int, input().split())
    time[i] = t
    for r in req:
        link[r].append(i)
        link_aq[i].append(r)

    if not req:
        q.append(i)
        visited[i] = t
        cnt += 1



while q:
    current = q.popleft()

    for e in link[current]:
        link_aq[e].remove(current)
        visited[e] = max(visited[e], visited[current])
        if not link_aq[e]:
            q.append(e)
            visited[e] += time[e]
            cnt += 1

for i in range(1, N+1):
    print(visited[i])