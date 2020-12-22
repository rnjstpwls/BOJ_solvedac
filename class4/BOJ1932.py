import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())

before = list(map(int, input().split()))
length = 2
for _ in range(n-1):
    numbers = list(map(int, input().split()))
    for i in range(1, length-1):
        numbers[i] += max(before[i-1], before[i])
    numbers[0] += before[0]
    numbers[-1] += before[-1]
    before = numbers
    length += 1

print(max(before))