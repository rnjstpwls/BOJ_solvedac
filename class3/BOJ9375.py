import sys


input = sys.stdin.readline
T = int(input())
for tc in range(T):
    n = int(input())
    clothes = dict()

    for _ in range(n):
        name, type = input().strip().split()
        if type in clothes:
            clothes[type] += 1
        else:
            clothes[type] = 1
    result = 1
    for i in clothes:
        result *= (clothes[i]+1)
    print(result-1)