import sys


def cause_youre_my_star(N):
    if N == 3:
        return ['  *  ', ' * * ', '*****']
    result = []
    tmp = cause_youre_my_star(N // 2)
    for line in tmp:
        result.append(' ' * (N // 2) + line + ' ' * (N // 2))
    for line in tmp:
        result.append(line + ' ' + line)

    return result


input = sys.stdin.readline

N = int(input())

print('\n'.join(cause_youre_my_star(N)))
