import sys
N = int(sys.stdin.readline())

info = []
for _ in range(N):
    info.append(tuple(map(int,sys.stdin.readline().split())))
# info.sort()
result = []
for i in range(N):
    cnt = 1
    for j in range(N):
        if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
            cnt += 1
    result.append(cnt)
print(*result)