import sys


N = int(sys.stdin.readline())

time = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
time.sort(key=lambda x: x[0])
time.sort(key=lambda x: x[1])

last = 0
cnt = 0

for s, e in time:
    if s >= last:
        cnt += 1
        last = e
print(cnt)