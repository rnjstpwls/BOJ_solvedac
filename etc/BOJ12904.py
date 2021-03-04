from collections import deque
import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

S = deque(input().strip())
T = deque(input().strip())
reverse = False
while len(T) > len(S):
    if reverse:
        if T[0] == 'A':
            T.popleft()
        else:
            T.popleft()
            reverse = False
    else:
        if T[-1] == 'A':
            T.pop()
        else:
            T.pop()
            reverse = True

if reverse:
    T.reverse()

if T == S:
    print(1)
else:
    print(0)