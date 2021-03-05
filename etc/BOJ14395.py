from collections import deque
import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

s, t = map(int, input().split())
if s == t:
    print(0)
    exit()
visited = set()
visited.add(s)
q = deque()
MAX_VALUE = 10e9
q.append((s, ''))

while q:
    cur, log = q.popleft()
    if cur == t:
        print(log)
        break
    if cur*cur not in visited and 0 <= cur*cur <= MAX_VALUE:
        q.append((cur*cur, log+'*'))
        visited.add(cur*cur)
    if cur+cur not in visited and 0 <= cur+cur <= MAX_VALUE:
        q.append((cur+cur, log+'+'))
        visited.add(cur+cur)

    if 1 not in visited and cur:
        q.append((1, log+'/'))
        visited.add(1)
else:
    print(-1)