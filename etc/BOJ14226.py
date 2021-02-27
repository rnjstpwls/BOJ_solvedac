from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

q = deque()
q.append((1, 0))

visited = dict()
visited[(1, 0)] = 0
while q:
    s, c = q.popleft()
    if s == n:
        print(visited[(s, c)])
        break
    if (s, s) not in visited.keys() and 1 <= s < 2001:
        visited[(s, s)] = visited[(s, c)] + 1
        q.append((s, s))
    if (s - 1, c) not in visited.keys() and 1 <= s - 1 < 1001 and 1 <= c < 2001:
        visited[(s - 1, c)] = visited[(s, c)] + 1
        q.append((s - 1, c))
    if (s + c, c) not in visited.keys() and 1 <= s + c < 1001 and 1 <= c < 2001:
        visited[(s + c, c)] = visited[(s, c)] + 1
        q.append((s + c, c))
