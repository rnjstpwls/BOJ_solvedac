import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline


dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16] + [0] * 88
for i in range(13, 101):
    dp[i] = dp[i-1] + dp[i-5]

T = int(input())

for _ in range(T):
    N = int(input())
    print(dp[N])