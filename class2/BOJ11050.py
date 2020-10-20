import sys
N, K = map(int, sys.stdin.readline().split())

factorial = [1, 1]
for i in range(2, 11):
    factorial.append(factorial[-1]*i)

print(factorial[N]//(factorial[K]*factorial[N-K]))