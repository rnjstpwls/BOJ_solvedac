import sys
K = int(sys.stdin.readline())

numbers = []
for _ in range(K):
    N = int(sys.stdin.readline())
    if N == 0:
        numbers.pop()
    else:
        numbers.append(N)
print(sum(numbers))