import sys

def search(val):
    left, right = 0, len(chicken) - 1
    while left < right:
        center = (left+right) // 2
        if chicken[center] < val:
            left = center + 1
        else:
            right = center
    return right


input = sys.stdin.readline

C, N = map(int, input().split())

chicken = sorted([int(input()) for _ in range(C)])
cow = [tuple(map(int, input().split())) for _ in range(N)]
cow.sort(key=lambda x: x[1])

result = 0

for i in range(N):
    if not chicken:
        break

    s = search(cow[i][0])
    if cow[i][0] <= chicken[s] <= cow[i][1]:
        result += 1
        chicken.remove(chicken[s])
print(result)