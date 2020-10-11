import sys
N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))

P.sort()

total = 0

for i in range(N):
    total += P[i] * (N-i)
print(total)