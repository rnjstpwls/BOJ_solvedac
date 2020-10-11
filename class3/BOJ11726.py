import sys
n = int(sys.stdin.readline())

if n == 1:
    print(1)
    exit()

result = [0] * (n+1)
result[1], result[2] = 1, 2

for i in range(3, n+1):
    result[i] = result[i-2] + result[i-1]
print(result[n]%10007)
