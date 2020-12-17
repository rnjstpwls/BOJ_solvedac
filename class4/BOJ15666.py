import sys
from itertools import combinations_with_replacement

sys.stdin = open('input.txt')

input = sys.stdin.readline

N, M = map(int, input().split())

numbers = sorted(list(map(int, input().split())))

for result in sorted(list(set(combinations_with_replacement(numbers, M)))):
    print(*result)