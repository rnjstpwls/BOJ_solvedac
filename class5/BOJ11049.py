import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())

numbers = list(tuple(map(int, input().split())) for _ in range(N))
print(numbers)

dp = [-1] * N
