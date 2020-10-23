import sys
from collections import deque


def search(r, c):
    q = deque()
    q.append((r, c, 0))
    visited = {(r, c)}
    while q:
        cr, cc, cnt = q.popleft()
        if (cr, cc) == (N-1, M-1):
            return cnt
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = cr+dr, cc+dc
            if not(0 <= nr < N) or not(0 <= nc < M) or not arr[nr][nc] or (nr, nc) in visited:
                continue
            q.append((nr, nc, cnt+1))
            visited.add((nr, nc))
    pass


N, M = map(int, sys.stdin.readline().split())
arr = list(list(map(int,list(sys.stdin.readline().strip()))) for _ in range(N))
print(search(0, 0)+1)