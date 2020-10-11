import sys
sys.setrecursionlimit(10**6)

def search(r, c):
    if not arr[r][c] or (r, c) in visited:
        return False

    visited.add((r, c))

    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nr, nc = r+dr, c+dc
        if not(0 <= nr < N) or not(0 <= nc < M):
            continue
        else:
            search(nr, nc)
    return True


T = int(sys.stdin.readline())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    arr = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        arr[y][x] = 1
    visited = set()
    total = 0

    for i in range(N):
        for j in range(M):
            if search(i, j):
                total += 1

    print(total)