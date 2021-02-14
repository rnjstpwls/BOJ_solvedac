from collections import deque

N, K = map(int, input().split())


q = deque()
visited = [-1] * 100001
visited[N] = 0

q.append(N)

while q:
    x = q.popleft()
    if x == K:
        move = [x]
        while True:
            if x == N:
                break
            move.append(visited[x])
            x = visited[x]
        print(len(move)-1)
        print(*move[::-1])
        break
    for nx in [2 * x, x + 1, x - 1]:
        if 0 <= nx < 100001 and visited[nx] == -1:
            q.append(nx)
            visited[nx] = x
