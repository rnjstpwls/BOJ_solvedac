import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
*number, sol = map(int, input().split())

dp = [[0]*21 for _ in range(N-1)]
dp[0][number[0]] = 1
for i in range(1, N-1):
    for j in range(21):
        if dp[i-1][j]:
            if 0 <= j + number[i] <= 20:
                dp[i][j+number[i]] += dp[i-1][j]
            if 0 <= j - number[i] <= 20:
                dp[i][j-number[i]] += dp[i-1][j]
print(dp[-1][sol])