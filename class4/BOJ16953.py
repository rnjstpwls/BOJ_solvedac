import sys
from collections import deque

A, B = map(int, sys.stdin.readline().split())

q = deque()
q.append((A, 1))

result = -1
while q:
    current, cnt = q.popleft()
    if current == B:
        result = cnt
        break
    value1, value2 = current*2, current*10+1
    if value1 <= B:
        q.append((value1, cnt+1))
    if value2 <= B:
        q.append((value2, cnt+1))

print(result)