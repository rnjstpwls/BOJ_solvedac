import sys


def matrix(n):
    if n == 1:
        return BASE_MATRIX

    if n % 2:
        return gemm(matrix(n - 1), BASE_MATRIX)
    else:
        return gemm_square(matrix(n // 2))


def gemm(m1, m2):
    return [
        [(m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]) % 100, (m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]) % 100],
        [(m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]) % 100, (m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]) % 100]
    ]


def gemm_square(m1):
    return gemm(m1, m1)


sys.stdin = open('input.txt')

input = sys.stdin.readline

x, y, a0, a1, n = map(int, input().split())

BASE_MATRIX = [[x, y], [1, 0]]

if n == 0:
    print(a0)
elif n == 1:
    print(a1)
else:
    result = matrix(n-1)
    print(f'{(result[0][0]*a1 + result[0][1]*a0) % 100 :02d}')