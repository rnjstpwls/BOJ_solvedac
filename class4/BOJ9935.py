import sys

input = sys.stdin.readline

text = input().strip()
bomb = input().strip()

key = bomb[-1]
length = len(bomb)

stack = []

for t in text:
    stack.append(t)
    if t == key and ''.join(stack[-length:]) == bomb:
        del stack[-length:]
if stack:
    print(''.join(stack))
else:
    print('FRULA')
