import sys


N, M = map(int, sys.stdin.readline().split())


poketmon = [None] * (N+1)
poketdict = dict()
for i in range(1, N+1):
    poketmon[i] = sys.stdin.readline().strip()
    poketdict[poketmon[i]] = i

result = []

for _ in range(M):
    txt = sys.stdin.readline().strip()
    if ord('1') <= ord(txt[0]) <= ord('9'):
        result.append(poketmon[int(txt)])
    else:
        result.append(poketdict[txt])
for i in result:
    print(i)
