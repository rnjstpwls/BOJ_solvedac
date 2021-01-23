import sys


input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

tmp = 0
result = -sys.maxsize

for i in range(N):
    tmp = max(tmp+numbers[i], numbers[i])
    result = max(result, tmp)

print(result)