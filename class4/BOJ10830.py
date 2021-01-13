import sys


def solve(cnt):
    if cnt == 1:
        return matrix

    if cnt % 2:
        return matrix_multiplication(solve(cnt-1), matrix)
    else:
        return matrix_square(solve(cnt//2))


def matrix_multiplication(arr1, arr2):
    result = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            for i in range(N):
                result[r][c] += arr1[r][i] * arr2[i][c]
            result[r][c] %= 1000
    return result


def matrix_square(arr):
    result = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            for i in range(N):
                result[r][c] += arr[r][i] * arr[i][c]
            result[r][c] %= 1000
    return result


input = sys.stdin.readline

N, B = map(int, input().split())

matrix = [list(map(lambda x: int(x)%1000, input().split())) for _ in range(N)]

for row in solve(B):
    print(*row)