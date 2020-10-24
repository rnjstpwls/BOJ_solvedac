import sys
from collections import deque


def check(r, c):
    return 0 <= r < N and 0 <= c < M


def result():
    answer = 0
    for r in range(N):
        for c in range(M):
            if farm[r][c] == 0:
                return -1
            else:
                answer = max(answer, farm[r][c])
    return answer-1


M, N = map(int, sys.stdin.readline().split())
farm = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))

q = deque()

for i in range(N):
    for j in range(M):
        if farm[i][j] == 1:
            q.append((i, j))


while q:
    cr, cc = q.popleft()

    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nr, nc = cr+dr, cc+dc
        if check(nr, nc) and farm[nr][nc] == 0:
            farm[nr][nc] = farm[cr][cc] + 1
            q.append((nr, nc))


print(result())