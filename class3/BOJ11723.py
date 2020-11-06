import sys

input = sys.stdin.readline

M = int(input())

A = set()

for _ in range(M):
    command, *value = input().split()
    # print(command, value)

    if value:
        value = int(value[0])

    if command == 'add':
        A.add(value)
    elif command == 'remove':
        A.discard(value)
    elif command == 'check':
        if value in A:
            print(1)
        else:
            print(0)
    elif command == 'toggle':
        if value in A:
            A.discard(value)
        else:
            A.add(value)
    elif command == 'all':
        A = set(list(range(1, 21)))
    else:
        A = set()
