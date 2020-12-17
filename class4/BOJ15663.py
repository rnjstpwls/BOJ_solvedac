import sys
from itertools import permutations

sys.stdin = open('input.txt')

input = sys.stdin.readline

N, M = map(int, input().split())

numbers = list(map(int, input().split()))
result = sorted(list(set(permutations(numbers, M))))
for res in result:
    print(*res)