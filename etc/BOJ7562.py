import sys
from collections import deque

sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())

d = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

for _ in range(T):
    l = int(input())
    start_r, start_c = map(int, input().split())
    end_r, end_c = map(int, input().split())
    visited = [[False] * l for _ in range(l)]
    visited[start_r][start_c] = True
    q = deque()
    q.append((start_r, start_c, 0))
    while q:
        cr, cc, cnt = q.popleft()

        if (cr, cc) == (end_r, end_c):
            print(cnt)
            break

        for dr, dc in d:
            nr, nc = cr+dr, cc+dc
            if (0 <= nr < l) and (0 <= nc < l) and not visited[nr][nc]:
                q.append((nr, nc, cnt+1))
                visited[nr][nc] = True