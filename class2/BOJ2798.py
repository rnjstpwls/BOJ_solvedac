import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
result = []

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            tmp = numbers[i]+numbers[j]+numbers[k]
            if tmp > M:
                continue
            else:
                result.append(tmp)

print(max(result))

