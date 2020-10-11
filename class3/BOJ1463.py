import sys
N = int(sys.stdin.readline())

result = [0] * (N+1)

for i in range(2, N+1):
    if i % 3 == 0:
        result[i] = min(result[i-1]+1, result[i//3]+1)
    elif i % 2 == 0:
        result[i] = min(result[i-1]+1, result[i//2]+1)
    else:
        result[i] = result[i-1] + 1

print(result[N])