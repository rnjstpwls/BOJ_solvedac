import sys
import heapq


def dijkstra(p):
    dist = [9876543210] * (n+1)
    dist[p] = 0
    heap = [(0, p)]

    while heap:
        val, cur = heapq.heappop(heap)

        if dist[cur] < val:
            continue

        for next, v in link[cur]:
            nv = v + val
            if nv < dist[next]:
                dist[next] = nv
                heapq.heappush(heap, (nv, next))

    cnt, last = 0, 0

    for i in range(1, n+1):
        if dist[i] != 9876543210:
            last = max(last, dist[i])
            cnt += 1
    return (cnt, last)

sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, d, c = map(int, input().split())
    link = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        link[b].append((a, s))
    print(*dijkstra(c))