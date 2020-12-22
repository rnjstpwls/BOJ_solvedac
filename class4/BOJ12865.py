import sys

input = sys.stdin.readline

N, K = map(int, input().split())

weight = [0] * (K + 1)

for _ in range(N):
    new_weight = [0] * (K + 1)
    W, V = map(int, input().split())

    for i in range(K + 1):
        if i - W >= 0:
            new_weight[i] = max(weight[i], weight[i - W] + V)
        else:
            new_weight[i] = weight[i]
    weight = new_weight
print(max(weight))
