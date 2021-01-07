import sys
from collections import deque

def search(r, c):
    q = deque()
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
    q.append((r, c, 1))
    visited[r][c][1] = 1

    while q:
        cr, cc, chance = q.popleft()
        if (cr, cc) == (N-1, M-1):
            return visited[cr][cc][chance]

        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = cr+dr, cc+dc

            if (0 <= nr < N) and (0 <= nc < M):
                if arr[nr][nc] == '1' and chance:
                    q.append((nr, nc, 0))
                    visited[nr][nc][0] = visited[cr][cc][1] + 1

                if arr[nr][nc] == '0' and visited[nr][nc][chance] == 0:
                    q.append((nr, nc, chance))
                    visited[nr][nc][chance] = visited[cr][cc][chance] + 1
    return -1


sys.stdin = open('input.txt')

input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(input().strip() for _ in range(N))
# print(arr)
print(search(0, 0))