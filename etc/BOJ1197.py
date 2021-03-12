import sys
import heapq

sys.stdin = open('input.txt')

input = sys.stdin.readline

V, E = map(int, input().split())
link = [[] for _ in range(V+1)]
for _ in range(E):
    A, B, C = map(int, input().split())
    link[A].append((B, C))
    link[B].append((A, C))

visited = [False] * (V+1)
heap = [(0, 1)]
result = 0
while heap:
    cv, cd = heapq.heappop(heap)
    if visited[cd]:
        continue
    result += cv
    visited[cd] = True
    for nd, nv in link[cd]:
        if not visited[nd]:
            heapq.heappush(heap, (nv, nd))
print(result)