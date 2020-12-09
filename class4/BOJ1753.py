import sys
import heapq

inf = 3000001

def dijkstra(point):
    heap = []
    distance = [inf] * (V + 1)
    distance[point] = 0

    heapq.heappush(heap, (0, point))

    while heap:
        value, destination = heapq.heappop(heap)
        if distance[destination] < value:
            continue

        for val, des in link[destination]:
            total = val + value
            if total < distance[des]:
                distance[des] = total
                heapq.heappush(heap, (total, des))
    return distance


sys.stdin = open('input.txt')

input = sys.stdin.readline

V, E = map(int, input().split())
START_POINT = int(input())
link = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    link[u].append((w, v))

result = dijkstra(START_POINT)

for i in range(1, V + 1):
    if result[i] == inf:
        print('INF')
    else:
        print(result[i])
