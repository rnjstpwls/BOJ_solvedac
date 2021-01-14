import sys

input = sys.stdin.readline

N = int(input())

dp = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for _ in range(N - 1):
    new = [0] * 10
    new[0] += dp[1]
    for i in range(1, 9):
        new[i] += dp[i - 1]
        new[i] += dp[i + 1]
    new[9] += dp[8]
    dp = new

print(sum(dp) % 1_000_000_000)
