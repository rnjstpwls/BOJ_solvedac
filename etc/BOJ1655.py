import sys
import heapq
sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
left, right = [], []
for i in range(N):
    Z = int(input())
    if len(left) == len(right):
        heapq.heappush(left, -Z)
    else:
        heapq.heappush(right, Z)

    if right and -left[0] > right[0]:
        lv = heapq.heappop(left)
        rv = heapq.heappop(right)
        heapq.heappush(left, -rv)
        heapq.heappush(right, -lv)
    print(-left[0])