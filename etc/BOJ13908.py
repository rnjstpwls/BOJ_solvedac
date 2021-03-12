import sys

def check():
    for n in num:
        if not visited[n]:
            return False
    return True


def search(idx):
    global result
    if idx == n:
        if check():
            result += 1
        return

    for i in range(10):
        visited[i] += 1
        search(idx+1)
        visited[i] -= 1
    pass


sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
visited = [0] * 10
result = 0
search(0)
print(result)