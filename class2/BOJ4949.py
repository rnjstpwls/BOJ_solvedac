import sys


while True:
    text = sys.stdin.readline().rstrip()
    # print(text)
    if text == '.':
        break

    result = True

    stack = []
    for t in text:
        if t == '(' or t == '[':
            stack.append(t)
            # print(stack)
        elif t == ')':
            if not stack:
                result = False
                break
            else:
                tmp = stack.pop()
                if tmp == '(':
                    continue
                else:
                    result = False
                    break
            pass
        elif t == ']':
            if not stack:
                result = False
                break
            else:
                tmp = stack.pop()
                if tmp == '[':
                    continue
                else:
                    result = False
                    break
            pass
        elif t == '.':
            break
        else:
            continue
    if stack or not result:
        print('no')
    else:
        print('yes')