import sys
from collections import deque


def bfs():
    q = deque()
    visited = [[[False] * M for _ in range(N)] for _ in range(H)]
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if arr[h][n][m] == 1:
                    q.append((h, n, m, 0))
                    visited[h][n][m] = True

    while q:
        ch, cr, cc, cnt = q.popleft()

        for dh, dr, dc in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
            nh, nr, nc = ch + dh, cr + dr, cc + dc
            if (0 <= nh < H) and (0 <= nr < N) and (0 <= nc < M) and not visited[nh][nr][nc] and arr[nh][nr][nc] != -1:
                arr[nh][nr][nc] = 1
                visited[nh][nr][nc] = True
                q.append((nh, nr, nc, cnt + 1))
    return cnt


def check():
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if arr[h][r][c] == 0:
                    return False
    return True


sys.stdin = open('input.txt')

input = sys.stdin.readline

M, N, H = map(int, input().split())
arr = list(list(list(map(int, input().split())) for _ in range(N)) for _ in range(H))

ans = bfs()

if check():
    print(ans)
else:
    print(-1)
