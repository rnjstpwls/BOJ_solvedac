import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    printer = deque(map(int, sys.stdin.readline().split()))
    for i in range(N):
        printer[i] = (printer[i], i)

    cnt = 1
    while printer:
        current, idx = printer.popleft()
        for i in range(len(printer)):
            if printer[i][0] > current:
                printer.append((current, idx))
                break
        else:
            if idx == M:
                print(cnt)
            cnt += 1

