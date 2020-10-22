import sys


N = int(sys.stdin.readline())
stairs = list(int(sys.stdin.readline()) for _ in range(N))
if N <= 2:
    print(sum(stairs))
    exit()
result = []
result.append(stairs[0])
result.append(stairs[1] + stairs[0])
result.append(max(stairs[0]+stairs[2], stairs[1]+stairs[2]))
for i in range(3, N):
    result.append(max(stairs[i] + stairs[i-1] + result[i-3], stairs[i] + result[i-2]))
print(result[-1])