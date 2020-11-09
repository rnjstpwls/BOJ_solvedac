import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    if x > 0:
        heapq.heappush(heap, (x, 1))
    elif x < 0:
        heapq.heappush(heap, (-x, -1))
    else:
        if heap:
            value, sign = heapq.heappop(heap)
            print(value*sign)
        else:
            print(0)