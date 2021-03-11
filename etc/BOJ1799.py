import sys


def oddsearch(idx, cnt):
    global oddresult
    if idx == oddlength:
        oddresult = max(oddresult, cnt)
        return
    cr, cc = oddboard[idx]
    oddsearch(idx + 1, cnt)
    if not slash[cr + cc] and not backslash[cc - cr + N - 1]:
        slash[cr + cc] = True
        backslash[cc - cr + N - 1] = True
        oddsearch(idx + 1, cnt + 1)
        slash[cr + cc] = False
        backslash[cc - cr + N - 1] = False


def evensearch(idx, cnt):
    global evenresult
    if idx == evenlength:
        evenresult = max(evenresult, cnt)
        return
    cr, cc = evenboard[idx]
    evensearch(idx + 1, cnt)
    if not slash[cr + cc] and not backslash[cc - cr + N - 1]:
        slash[cr + cc] = True
        backslash[cc - cr + N - 1] = True
        evensearch(idx + 1, cnt + 1)
        slash[cr + cc] = False
        backslash[cc - cr + N - 1] = False


sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
arr = list(list(map(int, input().split())) for _ in range(N))
oddboard = []
evenboard = []
for r in range(N):
    for c in range(N):
        if arr[r][c]:
            if (r + c) % 2:
                oddboard.append((r, c))
            else:
                evenboard.append((r, c))

slash = [False] * (2 * N - 1)
backslash = [False] * (2 * N - 1)
oddlength = len(oddboard)
evenlength = len(evenboard)
oddresult = 0
evenresult = 0
oddsearch(0, 0)
evensearch(0, 0)
print(oddresult+evenresult)
