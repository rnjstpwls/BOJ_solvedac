import sys


def power(a, b):
    if b == 1:
        return a % C
    if b == 0:
        return 1

    if b % 2:
        return power(a, b-1) * a % C
    else:
        return power(a, b//2) ** 2 % C



input = sys.stdin.readline

A, B, C = map(int, input().split())

print(power(A, B) % C)