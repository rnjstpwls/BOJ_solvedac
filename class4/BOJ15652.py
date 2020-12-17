def search(idx, arr):
    if len(arr) == M:
        print(*arr)
        return
    if idx == N:
        return

    search(idx, arr+[numbers[idx]])
    search(idx+1, arr)


N, M = map(int, input().split())

numbers = list(range(1, N + 1))

search(0, [])