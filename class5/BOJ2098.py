import sys


def TSP(cur, visited):
    if visited == (1 << N) - 1:
        return W[cur][0] if W[cur][0] else inf

    if dp[cur][visited] != -1:
        return dp[cur][visited]

    cost = inf
    for next in range(1, N):
        if visited & (1 << next) or not W[cur][next]:
            continue
        cost = min(cost, TSP(next, visited | 1 << next) + W[cur][next])
    dp[cur][visited] = cost
    return cost


sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
W = list(list(map(int, input().split())) for _ in range(N))

dp = [[-1] * ((1 << N) - 1) for _ in range(N)]
inf = sys.maxsize
print(TSP(0, 1))