import sys
import heapq


def dijkstra(start, end):
    inf = float('inf')
    dist = [inf] * (N+1)
    heap = [(0, start)]

    while heap:
        value, destination = heapq.heappop(heap)

        if value > dist[destination]:
            continue

        for v, d in link[destination]:
            total = value + v
            if total < dist[d]:
                dist[d] = total
                heapq.heappush(heap, (total, d))
    return dist[end]


sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
M = int(input())
link = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, v = map(int, input().split())
    link[s].append((v, e))

start, end = map(int, input().split())

print(dijkstra(start, end))