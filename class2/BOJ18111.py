import sys


N, M, B = map(int, sys.stdin.readline().split())

ground = []
for _ in range(N):
    ground += list(map(int, sys.stdin.readline().split()))

height = [0] * 257

for g in ground:
    height[g] += 1

result = float('inf')
idx = 0

for i in range(min(ground), (sum(ground)+B)//(N*M) + 1):
    tmp = 0
    for j in range(257):
        if height[j]:
            if i > j:
                tmp += (i-j)*height[j]
            else:
                tmp += 2*(j-i)*height[j]
    if tmp <= result:
        result = tmp
        idx = i
print(result, idx)