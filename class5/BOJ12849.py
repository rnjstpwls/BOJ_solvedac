import sys

input = sys.stdin.readline

link = [
    [1, 2],
    [0, 2, 3],
    [0, 1, 3, 5],
    [1, 2, 4, 5],
    [3, 5, 6],
    [2, 3, 4, 7],
    [4, 7],
    [5, 6]
]

D = int(input())
D += 1
dp = [[0] * D for _ in range(8)]
dp[0][0] = 1
for d in range(1, D):
    for cur in range(8):
        for next in link[cur]:
            dp[next][d] = (dp[next][d] + dp[cur][d - 1]) % 1_000_000_007

print(dp[0][-1])
