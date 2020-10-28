import sys


N, K = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for _ in range(N)]
coin.reverse()

idx = 0
result = 0
while K > 0:
    current = coin[idx]
    result += (K//current)
    K %= current
    idx += 1

print(result)