import sys
N = int(sys.stdin.readline())
sg = list(map(int, sys.stdin.readline().split()))

positive = [0] * 10000001
negative = [0] * 10000001

for s in sg:
    if s >=0:
        positive[s] += 1
    else:
        negative[-s] += 1

M = int(sys.stdin.readline())
cnt = list(map(int, sys.stdin.readline().split()))
result = []
for c in cnt:
    if c >=0:
        result.append(positive[c])
    else:
        result.append(negative[-c])
print(*result)