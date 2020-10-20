import sys

N = int(sys.stdin.readline())

board = []
for _ in range(N):
    board.append(tuple(map(int, sys.stdin.readline().split())))

board.sort()

for i in board:
    print(*i)