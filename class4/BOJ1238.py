import heapq
import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

N, M, X = map(int, input().split())

link = [[] for _ in range(N+1)]
link_reverse = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, cost = map(int, input().split())
    link[start].append((cost, end))
    link_reverse[end].append((cost, start))

heap = []
heap_reverse = []

for element in link[X]:
    heapq.heappush(heap,element)

for element in link_reverse[X]:
    heapq.heappush(heap_reverse,element)


visited = [-1] * (N+1)
visited[X] = 0
visited_reverse = [-1] * (N+1)
visited_reverse[X] = 0

cnt = 1
while heap:
    if cnt == N:
        break
    value, destination = heapq.heappop(heap)
    if visited[destination] != -1:
        continue

    visited[destination] = value
    for cost, end in link[destination]:
        if visited[end] == -1:
            heapq.heappush(heap, (cost+value, end))
    cnt += 1

cnt = 1
while heap_reverse:
    if cnt == N:
        break
    value, destination = heapq.heappop(heap_reverse)
    if visited_reverse[destination] != -1:
        continue

    visited_reverse[destination] = value
    for cost, end in link_reverse[destination]:
        if visited_reverse[end] == -1:
            heapq.heappush(heap_reverse, (cost+value, end))
    cnt += 1

print(max([a+b for a, b in zip(visited, visited_reverse)]))