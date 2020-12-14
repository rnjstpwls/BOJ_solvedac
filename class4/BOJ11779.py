import sys
import heapq


def dijkstra(start, end):
    inf = float('inf')
    dist = [[inf, None] for _ in range(n + 1)]
    dist[start][1] = [start]
    heap = [(0, start)]
    while heap:
        cost, destination = heapq.heappop(heap)

        if dist[destination][0] < cost:
            continue

        log = dist[destination][1]

        for c, d in link[destination]:
            total = cost + c
            if total < dist[d][0]:
                dist[d][0] = total
                dist[d][1] = log + [d]
                heapq.heappush(heap, (total, d))
    return dist[end]


sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
m = int(input())

link = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, v = map(int, input().split())
    link[s].append((v, e))

s, e = map(int, input().split())
total, log  = dijkstra(s, e)
print(total)
print(len(log))
print(*log)
