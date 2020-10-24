import sys


def check(arr):

    result = arr[0][0]
    for row in arr:
        for ele in row:
            if ele != result:
                for li in divide(arr):
                    check(li)
                return
    cnt[result+1] += 1

    pass


def divide(arr):
    div_paper = []
    size = len(arr)
    for r in range(3):
        for c in range(3):
            tmp = []
            for w in range(size//3):
                tmp.append(arr[r*size//3 + w][c*size//3:(c+1)*size//3])
            div_paper.append(tmp)
    return div_paper


input = sys.stdin.readline

N = int(input())
paper = list(list(map(int, input().split())) for _ in range(N))

cnt = [0] * 3
check(paper)

for c in cnt:
    print(c)