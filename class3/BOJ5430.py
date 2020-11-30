import sys


def AC(s, n, a):
    s.replace('RR', '')
    l, r, d = 0, 0, True
    for i in s:
        if i == 'R':
            d = not d
        elif i == 'D':
            if d:
                l += 1
            else:
                r += 1
    if l + r <= n:
        res = a[l:n - r]
        if d:
            return '[' + ','.join(res) + ']'
        else:
            return '[' + ','.join(res[::-1]) + ']'
    else:
        return 'error'


t = int(sys.stdin.readline())
for i in range(t):
    s = sys.stdin.readline()
    n = int(sys.stdin.readline())
    a = sys.stdin.readline().rstrip()[1:-1].split(',')
    print(AC(s, n, a))
