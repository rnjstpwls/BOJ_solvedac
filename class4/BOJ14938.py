import sys
import heapq


def dijkstra(first):
    inf = 987654321
    dist = [inf] * (n + 1)
    dist[first] = 0
    heap = [(0, first)]

    while heap:
        val, des = heapq.heappop(heap)
        if val > dist[des]:
            continue
        for v, d in link[des]:
            total = val+v
            if total <= m and total < dist[d]:
                heapq.heappush(heap, (total, d))
                dist[d] = total
    result = 0
    for i in range(1, n+1):
        if dist[i] <= m:
            result += items[i]
    return result

sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
link = [[] for _ in range(n + 1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    link[a].append((l, b))
    link[b].append((l, a))

answer = 0
for i in range(1, n+1):
    answer = max(answer, dijkstra(i))
print(answer)