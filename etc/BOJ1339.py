import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
dp = [0] * 26
cal = ord('A')
for _ in range(N):
    digit = 1
    for c in reversed(input().strip()):
        dp[ord(c)-cal] += digit
        digit *= 10
A = sorted(dp, reverse=True)[0:9]

B = list(range(9,0,-1))
print(sum(map(lambda x: x[0]*x[1], zip(A,B))))