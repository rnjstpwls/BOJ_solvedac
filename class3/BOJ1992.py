import sys


def quard_tree(arr, N):
    if check(arr, N)[0]:
        print(arr[0][0])
        return
    L = N // 2
    print('(', end='')
    # LT
    tmp = []
    for r in range(L):
        tmp.append(arr[r][:L])
    result = check(tmp, L)
    if result[0]:
        print(result[1], end='')
    else:
        quard_tree(tmp, L)
    # RT
    tmp = []
    for r in range(L):
        tmp.append(arr[r][L:])
    result = check(tmp, L)
    if result[0]:
        print(result[1], end='')
    else:
        quard_tree(tmp, L)
    # LB
    tmp = []
    for r in range(L):
        tmp.append(arr[L+r][:L])
    result = check(tmp, L)
    if result[0]:
        print(result[1], end='')
    else:
        quard_tree(tmp, L)
    # RB
    tmp = []
    for r in range(L):
        tmp.append(arr[L+r][L:])
    result = check(tmp, L)
    if result[0]:
        print(result[1], end='')
    else:
        quard_tree(tmp, L)
    print(')', end='')
    pass


def check(arr, L):
    tmp = arr[0][0]
    for r in range(L):
        for c in range(L):
            if tmp != arr[r][c]:
                return (False, -1)
    return (True, tmp)


# sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
arr = list(input().strip() for _ in range(N))
quard_tree(arr, N)