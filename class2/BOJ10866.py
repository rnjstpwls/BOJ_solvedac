import sys
from collections import deque
N = int(sys.stdin.readline())

stack = deque()

for _ in range(N):
    command, *etc = sys.stdin.readline().split()

    if command == 'push_front':
        stack.appendleft(etc[0])
    elif command == 'push_back':
        stack.append(etc[0])
    elif command == 'pop_front':
        if not stack:
            print(-1)
        else:
            print(stack.popleft())
    elif command == 'pop_back':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif command == 'front':
        if not stack:
            print(-1)
        else:
            print(stack[0])
    elif command == 'back':
        if not stack:
            print(-1)
        else:
            print(stack[-1])