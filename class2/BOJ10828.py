import sys
N = int(sys.stdin.readline())

stack = []

for _ in range(N):
    command, *etc = sys.stdin.readline().split()

    if command == 'push':
        stack.append(etc[0])
    elif command == 'pop':
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
    elif command == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])

