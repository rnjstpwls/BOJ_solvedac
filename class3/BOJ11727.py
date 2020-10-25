import sys


tile = [0, 1, 3] + [0]*998

for i in range(3, 1001):
    tile[i] = tile[i-1] + 2*tile[i-2]

print(tile[int(sys.stdin.readline())]%10007)