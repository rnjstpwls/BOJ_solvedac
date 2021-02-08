import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    root = [0] + list(map(int, input().split()))
    visited = [0] * (n + 1)
    cycle = 1
    for i in range(1, n + 1):
        if not visited[i]:
            while not visited[i]:
                visited[i] = cycle
                i = root[i]
            while visited[i] == cycle:
                visited[i] = -1
                i = root[i]
            cycle += 1
    print(n - visited.count(-1))
