import sys
from collections import deque


def dfs(point):
    dfs_result.append(point)
    for i in link[point]:
        if i not in dfs_result:
            dfs(i)


def bfs(point):
    q = deque()
    q.append(point)
    bfs_result.append(point)

    while q:
        current = q.popleft()
        for i in link[current]:
            if i not in bfs_result:
                q.append(i)
                bfs_result.append(i)
    pass


input = sys.stdin.readline

N, M, V = map(int, input().split())

link = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    link[A].append(B)
    link[B].append(A)
for arr in link:
    arr.sort()
dfs_result = []
bfs_result = []
dfs(V)
bfs(V)
print(*dfs_result)
print(*bfs_result)