import sys
import heapq

inf = 987654321


def dijkstra():
    dist = [inf] * N
    history = [set()] * N
    heap = []
    for i in range(N):
        if status[i] == 'Y':
            dist[i] = 0
            heap.append((0, i))
    while heap:
        value, destination = heapq.heappop(heap)

        if dist[destination] < value:
            continue

        log = history[destination]
        for i in range(N):
            total = value + arr[destination][i]
            if total < dist[i]:
                dist[i] = total
                history[i] = log | {i}
                heapq.heappush(heap, (total, i))
    for i in range(N):
        if status[i] == 'Y':
            history[i] = {i}
    return list(zip(dist, history))


def search(idx, log, total):
    global answer
    if answer < total:
        return
    if idx == N:
        if len(log) >= P:
            answer = min(answer, total)
        return
    if cost[idx][0] != inf and not (cost[idx][1] & log):
        search(idx+1, log | cost[idx][1], total + cost[idx][0])
    search(idx+1, log, total)



sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

status = list(input().strip())

P = int(input())

cost = dijkstra()
print(cost)
answer = inf

search(0, set(), 0)

if answer == inf:
    print(-1)
else:
    print(answer)