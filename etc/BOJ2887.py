import sys


def find(point):
    if parent[point] == point:
        return point

    parent[point] = find(parent[point])
    return parent[point]


def union(p1, p2):
    r1 = find(p1)
    r2 = find(p2)

    if r1 == r2:
        return False

    parent[r1] = r2
    return True


sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
dist = []
arr = list(list(map(int, input().split())) + [i] for i in range(N))

parent = [x for x in range(N)]


arr.sort()
for i in range(N-1):
    dist.append((abs(arr[i][0]-arr[i+1][0]), arr[i][3], arr[i+1][3]))
arr.sort(key=lambda x:x[1])
for i in range(N-1):
    dist.append((abs(arr[i][1]-arr[i+1][1]), arr[i][3], arr[i+1][3]))
arr.sort(key=lambda x:x[2])
for i in range(N-1):
    dist.append((abs(arr[i][2]-arr[i+1][2]), arr[i][3], arr[i+1][3]))
dist.sort()

result = 0
for w, s, d in dist:
    if union(s, d):
        result += w
print(result)