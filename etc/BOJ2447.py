import sys


def printing_stars(N):
    if N == 1:
        return ['*']
    result = []
    block = printing_stars(N // 3)
    for line in block:
        result.append(line * 3)
    for line in block:
        result.append(line + ' ' * (N // 3) + line)
    for line in block:
        result.append(line * 3)
    return result


input = sys.stdin.readline
N = int(input())
print('\n'.join(printing_stars(N)))
