import sys

factorial = [0] * 501
factorial[0] = 1
for i in range(1, 501):
    factorial[i] = factorial[i-1]*i

N = factorial[int(sys.stdin.readline())]
result = 0
while N:
    if N % 10 == 0:
        result += 1
    else:
        break
    N //= 10
print(result)