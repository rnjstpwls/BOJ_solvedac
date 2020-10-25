import sys
from collections import deque


def search(r, c):
    q = deque([(r, c)])
    visited.add((r, c))
    cnt = 1
    while q:
        cr, cc = q.popleft()
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = cr+dr, cc+dc
            if not (0 <= nr < N) or not (0 <= nc < N) or (nr, nc) in visited or arr[nr][nc] == '0':
                continue
            q.append((nr, nc))
            visited.add((nr, nc))
            cnt += 1
    result.append(cnt)

    pass


N = int(sys.stdin.readline())
arr = list(list(sys.stdin.readline().strip()) for _ in range(N))
# print(arr)
result = []
visited = set()
for r in range(N):
    for c in range(N):
        if (r, c) not in visited and arr[r][c] == '1':
            search(r, c)

print(len(result))
for ele in sorted(result):
    print(ele)