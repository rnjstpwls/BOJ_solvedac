import sys
from collections import deque


def search(idx):
    q = deque()
    q.append((idx, 0))
    visited = {idx}
    result = 0
    while q:
        current, cnt = q.popleft()
        result += cnt
        for friend in link[current]:
            if friend not in visited:
                q.append((friend, cnt+1))
                visited.add(friend)
    return result

input = sys.stdin.readline

N, M = map(int, input().split())
link = [set() for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    link[A].add(B)
    link[B].add(A)

answer = 0
kevin = float('inf')
for i in range(1, N+1):
    if search(i) < kevin:
        kevin = search(i)
        answer = i
print(answer)