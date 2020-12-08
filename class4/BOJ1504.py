import sys
import heapq

sys.stdin = open('input.txt')

input = sys.stdin.readline

INF = 9876543210


def dijkstra(start):
    dist = [INF] * (N + 1)
    dist[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        value, destination = heapq.heappop(heap)
        if dist[destination] < value:
            continue

        for v, d in link[destination]:
            next_value = value + v
            if dist[d] > next_value:
                dist[d] = next_value
                heapq.heappush(heap, (next_value, d))
    return dist


N, E = map(int, input().split())

link = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    link[a].append((c, b))
    link[b].append((c, a))
v1, v2 = map(int, input().split())

A = dijkstra(v1)
B = dijkstra(v2)

result = min(A[1] + B[N], B[1] + A[N]) + A[v2]
if result >= INF:
    print(-1)
else:
    print(result)
