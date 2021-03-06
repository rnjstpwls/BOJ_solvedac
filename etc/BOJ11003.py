import sys
import heapq

sys.stdin = open('input.txt')

input = sys.stdin.readline

N, L = map(int, input().split())
A = list(map(int, input().split()))
# ans = [0] * N

heap = []
for i in range(L):
    heapq.heappush(heap, (A[i], i))
    # ans[i] = heap[0][0]
    print(heap[0][0], end=' ')
for i in range(L, N):
    heapq.heappush(heap, (A[i], i))
    while heap[0][1] <= i-L:
        heapq.heappop(heap)
    # ans[i] = heap[0][0]
    print(heap[0][0], end=' ')

# print(*ans)