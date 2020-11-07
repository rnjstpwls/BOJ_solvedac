import sys
from collections import deque

def search(idx):
    q = deque()
    q.append(idx)
    visited[idx] = True
    while q:
        current = q.popleft()
        for ele in link[current]:
            if not visited[ele]:
                q.append(ele)
                visited[ele] = True

input = sys.stdin.readline

N, M = map(int, input().split())
link = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    u, v = map(int, input().split())
    link[u].append(v)
    link[v].append(u)
cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        cnt += 1
        search(i)
print(cnt)