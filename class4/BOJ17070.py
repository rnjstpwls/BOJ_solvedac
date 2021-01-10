import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())

arr = list(list(map(int, input().split())) for _ in range(N))

garo = [[0]*N for _ in range(N)]
sero = [[0]*N for _ in range(N)]
slash = [[0]*N for _ in range(N)]

garo[0][1] = 1

for r in range(N):
    for c in range(N):
        if garo[r][c]:
            if c+1 < N and arr[r][c+1] == 0:
                garo[r][c+1] += garo[r][c]
                if r+1 < N and arr[r+1][c] == 0 and arr[r+1][c+1] == 0:
                    slash[r+1][c+1] += garo[r][c]
        if sero[r][c]:
            if r+1 < N and arr[r+1][c] == 0:
                sero[r+1][c] += sero[r][c]
                if c+1 < N and arr[r+1][c+1] == 0 and arr[r][c+1] == 0:
                    slash[r+1][c+1] += sero[r][c]
        if slash[r][c]:
            if c+1 < N and arr[r][c+1] == 0:
                garo[r][c+1] += slash[r][c]
            if r+1 < N and arr[r+1][c] == 0:
                sero[r+1][c] += slash[r][c]
            if r+1 < N and c+1 < N and arr[r][c+1] == 0 and arr[r+1][c] == 0 and arr[r+1][c+1] == 0:
                slash[r+1][c+1] += slash[r][c]

print(garo[-1][-1] + sero[-1][-1] + slash[-1][-1])