import sys

dp = [0] * 50001
square_number = [i ** 2 for i in range(1, 223)]
N = int(sys.stdin.readline())
dp[1] = 1

for i in range(2, N + 1):
    min_num, j = 4, 0

    while square_number[j] <= i:
        temp = i - square_number[j]
        min_num = min(min_num, dp[temp])
        j += 1

    dp[i] = min_num + 1

print(dp[N])