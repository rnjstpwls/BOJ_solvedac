import sys
N = int(sys.stdin.readline())
numbers = []
for _ in range(N):
    numbers.append(tuple(map(int, sys.stdin.readline().split())))
numbers.sort(key=lambda x: (x[1], x[0]))
for n in numbers:
    print(*n)