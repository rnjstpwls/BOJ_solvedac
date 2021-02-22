N = int(input())

dp = [0] * 101
dp[1], dp[2], dp[3], dp[4] = 1, 2, 3, 4

for i in range(5, 101):
    dp[i] = max(dp[i-3]*2, dp[i-4]*3, dp[i-5]*4, dp[i-1]+1)
print(dp[N])