import sys

def search():
    result = 0
    q = set([(0, 0, arr[0][0])])

    while q:
        r, c, alphabet = q.pop()
        if len(alphabet) == 26:
            return 26
        result = max(result, len(alphabet))

        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r+dr, c+dc
            if (0 <= nr < R) and (0 <= nc < C) and arr[nr][nc] not in alphabet:
                q.add((nr, nc, alphabet + arr[nr][nc]))
    return result

sys.stdin = open('input.txt')

input = sys.stdin.readline

R, C = map(int, input().split())
arr = list(input().strip() for _ in range(R))
print(search())
