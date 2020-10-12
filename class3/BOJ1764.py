import sys

N, M = map(int, sys.stdin.readline().split())

set_N = set()
set_M = set()

for _ in range(N):
    set_N.add(sys.stdin.readline().strip())

for _ in range(M):
    set_M.add(sys.stdin.readline().strip())

result = sorted(list(set_N & set_M))

print(len(result))
for i in result:
    print(i)
