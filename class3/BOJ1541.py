import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

eq = input().strip()
if '-' in eq:
    idx = eq.index('-')
    print(sum(map(int, eq[:idx].split('+'))) - sum(map(int, eq[idx + 1:].replace('-', '+').split('+'))))
else:
    numbers = list(map(int, eq.split('+')))
    print(sum(numbers))
