import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())

dp0, dp1 = 0, 1

for i in range(N-1):
    dp0, dp1 = dp0+dp1, dp0

print(dp0+dp1)