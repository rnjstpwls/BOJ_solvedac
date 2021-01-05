import sys


def MATRIX_MULTIPLICATION(arr1, arr2):
    result = [[0] * 8 for _ in range(8)]

    for r in range(8):
        for c in range(8):
            for i in range(8):
                result[r][c] += arr1[r][i] * arr2[i][c]
            result[r][c] %= 1_000_000_007
    return result


def MATRIX_SQUARE(arr):
    return MATRIX_MULTIPLICATION(arr, arr)


def solve(n):
    if n == 1:
        return arr

    if n % 2:
        return MATRIX_MULTIPLICATION(solve(n-1), arr)
    else:
        return MATRIX_SQUARE(solve(n//2))


input = sys.stdin.readline

arr = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 1, 0],
    [0, 0, 1, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0]
]

D = int(input())

BASE_MATRIX = [1, 0, 0, 0, 0, 0, 0, 0]

print(solve(D)[0][0])