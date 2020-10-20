import sys
T = int(sys.stdin.readline())

for _ in range(T):
    text = sys.stdin.readline()
    stack = []
    for t in text:
        if t == '(':
            stack.append(t)
        elif t == ')':
            if not stack:
                print('NO')
                break
            current = stack.pop()
            if current != '(':
                print('NO')
                break
            pass
        else:
            continue
    else:
        if stack:
            print('NO')
        else:
            print('YES')