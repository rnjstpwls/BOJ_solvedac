import sys
from collections import deque


def search(r, c):
    global total
    total += 1
    visited.add((r, c))
    color = arr[r][c]
    q = deque([(r, c)])

    while q:
        cr, cc = q.popleft()
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = cr+dr, cc+dc
            if not (0 <= nr < N) or not (0 <= nc < N) or (nr, nc) in visited or arr[nr][nc] != color:
                continue
            q.append((nr, nc))
            visited.add((nr, nc))

    pass


N = int(sys.stdin.readline())
arr = list(list(sys.stdin.readline().strip()) for _ in range(N))
# print(arr)
result = []

visited = set()
total = 0
for r in range(N):
    for c in range(N):
        if (r, c) not in visited:
            search(r, c)
result.append(total)

for r in range(N):
    for c in range(N):
        if arr[r][c] == 'G':
            arr[r][c] = 'R'
# print(arr)
visited = set()
total = 0
for r in range(N):
    for c in range(N):
        if (r, c) not in visited:
            search(r, c)
result.append(total)
print(*result)