from collections import deque

N, K = map(int, input().split())

if K <= N:
    print(N-K)
else:
    q = deque()
    visited = [-1] * 100001
    visited[N] = 0

    q.append(N)

    while q:
        x = q.popleft()
        if x == K:
            print(visited[K])
            break
        for nx in [2 * x, x + 1, x - 1]:
            if 0 <= nx < 100001 and visited[nx] == -1:
                if nx == 2 * x:
                    q.appendleft(nx)
                    visited[nx] = visited[x]
                else:
                    q.append(nx)
                    visited[nx] = visited[x] + 1
