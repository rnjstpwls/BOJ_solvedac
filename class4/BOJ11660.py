import sys
from itertools import accumulate

sys.stdin = open('input.txt')

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list([[0]*(N+1)]) + list([0]+list(accumulate(map(int, input().split()))) for _ in range(N))


for row in range(2, N+1):
    for col in range(1, N+1):
        arr[row][col] += arr[row-1][col]


result = []

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result.append((arr[x2][y2] - arr[x2][y1-1]) - (arr[x1-1][y2] - arr[x1-1][y1-1]))

for r in result:
    print(r)