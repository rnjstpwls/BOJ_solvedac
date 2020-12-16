import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    up = list(map(int, input().split()))
    down = list(map(int, input().split()))
    dp0 = [0] * n
    dp1 = [0] * n
    dp0[0], dp1[0] = up[0], down[0]
    dp0[1], dp1[1] = up[1]+down[0], up[0]+down[1]
    for i in range(2, n):
        dp0[i] = up[i] + max(dp1[i-1], dp0[i-2], dp1[i-2])
        dp1[i] = down[i] + max(dp0[i-1], dp0[i-2], dp1[i-2])

    print(max(dp0[-1], dp1[-1]))