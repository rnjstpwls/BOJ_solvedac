import sys
N, K = map(int, sys.stdin.readline().split())

circle = list(range(1, N+1))

result = []
idx = -1
while circle:
    idx = (idx + K) % len(circle)
    result.append(circle.pop(idx))
    idx -= 1
print('<',end='')
for i in range(N-1):
    print(result[i], end=', ')
print(result[-1],end='')
print('>')