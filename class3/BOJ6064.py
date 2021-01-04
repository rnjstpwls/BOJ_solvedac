import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    x, y = x - 1, y - 1
    ans = y + 1

    cx = y % M

    cnt = 0

    while cnt <= M:
        if cx == x:
            print(ans)
            break
        ans += N
        cx = (cx + N) % M
        cnt += 1
    else:
        print(-1)
