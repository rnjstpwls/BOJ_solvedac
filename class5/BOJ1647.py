import sys
import heapq

input = sys.stdin.readline


N, M = map(int, input().split())
link = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    link[a].append((c, b))
    link[b].append((c, a))

heap = []

visited = [False] * (N+1)
visited[1] = True
for element in link[1]:
    heapq.heappush(heap, element)

result = []
cnt = 1
while heap:
    v, destination = heapq.heappop(heap)
    if visited[destination]:
        continue
    result.append(v)
    visited[destination] = True
    cnt += 1
    if cnt == N:
        break

    for nextv, nextd in link[destination]:
        if not visited[nextd]:
            heapq.heappush(heap, (nextv, nextd))

print(sum(result)-max(result))