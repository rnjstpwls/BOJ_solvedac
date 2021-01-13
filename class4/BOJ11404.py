import sys
import heapq


def dijkstra(start):
    inf = float('inf')
    heap = [(0, start)]
    dist = [inf] * (n+1)
    dist[start] = 0
    while heap:
        val, des = heapq.heappop(heap)
        if dist[des] < val:
            continue

        for v, d in link[des]:
            total = val + v
            if total < dist[d]:
                heapq.heappush(heap, (total, d))
                dist[d] = total
    result = []
    for i in range(1, n+1):
        if dist[i] == inf:
            result.append(0)
        else:
            result.append(dist[i])
    return result


input = sys.stdin.readline

n = int(input())
m = int(input())
link = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    link[a].append((c, b))

dijkstra(2)

for i in range(1, n+1):
    print(*dijkstra(i))