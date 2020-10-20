import sys


n = int(sys.stdin.readline())
solution = list(int(sys.stdin.readline()) for _ in range(n))

number = 1
idx = 0
stack = []
result = []


while idx < n:
    if solution[idx] >= number:
        stack.append(number)
        result.append('+')
        number += 1
        continue

    if stack and stack[-1] == solution[idx]:
        stack.pop()
        result.append('-')
        idx += 1
        continue
    else:
        print('NO')
        break
else:
    for r in result:
        print(r)