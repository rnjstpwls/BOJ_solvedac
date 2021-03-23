import sys


def find(v):
    if parent[v] == v:
        return v

    parent[v] = find(parent[v])
    return parent[v]


def union(a, b):
    _a = find(a)
    _b = find(b)

    if _a == _b:
        return False
    else:
        if _a > _b:
            parent[_a] = _b
        else:
            parent[_b] = _a
        return True

def solve():
    result = 0
    for a, b, c in edge:
        if union(a, b):
            result += c
    return result

sys.stdin = open('input.txt')

input = sys.stdin.readline

V, E = map(int, input().split())

edge = list(tuple(map(int, input().split())) for _ in range(E))
edge.sort(key=lambda x: x[2])
parent = [i for i in range(V+1)]
print(solve())
