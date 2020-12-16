import sys
from itertools import permutations



sys.stdin = open('input.txt')

input = sys.stdin.readline

N, M = map(int, input().split())

numbers = sorted(list(map(int, input().split())))

for per in permutations(numbers, M):
    print(*per)