import sys
import heapq


def dijkstra(p):
    heap = [(0, p)]
    dist = [9876543210] * (V+1)
    dist[p] = 0
    while heap:
        v, cur = heapq.heappop(heap)

        if dist[cur] < v:
            continue

        for des, val in arr[cur]:
            total = v + val
            if total < dist[des]:
                dist[des] = total
                heapq.heappush(heap, (total, des))

    return dist

sys.stdin = open('input.txt')

input = sys.stdin.readline

V, E, P = map(int, input().split())
arr = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

MJ = dijkstra(1)
GW = dijkstra(P)
if MJ[V] == MJ[P] + GW[V]:
    print('SAVE HIM')
else:
    print('GOOD BYE')