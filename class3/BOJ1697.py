import sys

input = sys.stdin.readline

N, K = map(int, input().split())
position = [abs(i-N) for i in range(100002)]

for i in range(1, 100001):
    position[i] = min(position[i], position[i-1]+1, position[i+1]+1)
    if i*2 < 100001:
        position[i*2] = min(position[i*2], position[i]+1)
print(position[K])
