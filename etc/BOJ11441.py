from itertools import accumulate
import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline


N = int(input())
arr = list(accumulate([0] + list(map(int, input().split()))))
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(arr[b] - arr[a-1])