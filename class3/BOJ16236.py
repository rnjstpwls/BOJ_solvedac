import sys
from collections import deque


def find_shark():
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 9:
                return (r, c)


def search(r, c):
    global result, shark_size, fish_cnt
    q = deque()
    visited = [[False] * N for _ in range(N)]
    q.append((r, c, 1))
    visited[r][c] = True
    fish_candidate = []

    while q:
        cr, cc, length = q.popleft()

        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            nr, nc = cr + dr, cc + dc
            if (0 <= nr < N) and (0 <= nc < N) and not visited[nr][nc]:
                if arr[nr][nc] == 0 or arr[nr][nc] == shark_size:
                    q.append((nr, nc, length + 1))
                elif arr[nr][nc] < shark_size:
                    fish_candidate.append((nr, nc, length))
                visited[nr][nc] = True

    if fish_candidate:
        fish_candidate.sort(key=lambda x: (x[2], x[0], x[1]))
        sr, sc, length = fish_candidate[0]
        fish_cnt += 1
        if fish_cnt == shark_size:
            shark_size += 1
            fish_cnt = 0
        result += length
        arr[sr][sc] = 0

        return search(sr, sc)


sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())

arr = list(list(map(int, input().split())) for _ in range(N))

shark_r, shark_c = find_shark()
arr[shark_r][shark_c] = 0
result = 0
shark_size = 2
fish_cnt = 0
search(shark_r, shark_c)
print(result)
# for row in arr:
#     print(*row)
