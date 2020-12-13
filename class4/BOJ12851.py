import sys
from collections import deque

input = sys.stdin.readline

visited = [False] * 100001

N, K = map(int, input().split())
if N >= K:
    print(N-K)
    print(1)

else:
    q = deque()

    q.append((N, 0))

    result = float('inf')
    answer = 0

    while q:
        current, cnt = q.popleft()
        visited[current] = True
        if result < cnt:
            continue

        if current == K:
            result = cnt
            answer += 1
            continue

        if current < 100000 and not visited[current+1]:
            q.append((current+1, cnt+1))
        if 0 < current and not visited[current-1]:
            q.append((current-1, cnt+1))
        if current <= 50000 and not visited[current*2]:
            q.append((current*2, cnt+1))

    print(result)
    print(answer)