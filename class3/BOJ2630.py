from collections import deque
import sys


def check(arr):
    global cnt, white, blue
    size = len(arr)
    if size == 1:
        if arr[0][0] == 0:
            white += 1
        else:
            blue += 1
        return
    total = 0

    for row in arr:
        total += sum(row)

    if total == 0:
        white += 1
        return
    elif total == size * size:
        blue += 1
        return
    else:
        for i in range(2):
            for j in range(2):
                tmp = []
                for k in range(size // 2):
                    tmp.append(arr[(size // 2 * i) + k][size // 2 * j: size // 2 * (j + 1)])

                q.append(tmp)




input = sys.stdin.readline

N = int(input())
paper = list(list(map(int, input().split())) for _ in range(N))

q = deque()
q.append(paper)
white = blue = 0

while q:
    current = q.popleft()
    check(current)
print(white)
print(blue)
