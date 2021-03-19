import sys
import heapq


def solve():
    heap = []
    visited = [False] * m
    for next, value in link[0]:
        heapq.heappush(heap, (value, next))
    visited[0] = True
    result = 0
    cnt = 1
    while heap:
        val, cur = heapq.heappop(heap)
        if visited[cur]:
            continue
        result += val
        cnt += 1
        if cnt == m:
            break
        visited[cur] = True
        for nd, value in link[cur]:
            if not visited[nd]:
                heapq.heappush(heap, (value, nd))

    return result



sys.stdin = open('input.txt')

input = sys.stdin.readline

while True:
    m, n = map(int, input().split())
    if (m, n) == (0, 0):
        break

    link = [[] for _ in range(m)]
    total = 0
    for _ in range(n):
        x, y, z = map(int, input().split())
        link[x].append((y, z))
        link[y].append((x, z))
        total += z
    print(total - solve())
