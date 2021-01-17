import sys

def search(start, number):
    start = start+1
    end = N-1
    result = sys.maxsize
    return_value = sys.maxsize
    while start <= end:
        center = (start+end)//2
        calculate = number + numbers[center]
        if abs(result) > abs(calculate):
            return_value = numbers[center]
            result = abs(calculate)
        if calculate < 0:
            start = center+1
        elif calculate > 0:
            end = center-1
        else:
            print(number, numbers[center])
            exit()
    return (number, return_value)


sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

answer = (0, 0)
max_value = sys.maxsize
for i in range(N):
    a, b = search(i, numbers[i])

    if max_value > abs(a+b):
        answer = (a, b)
        max_value = abs(a+b)

print(*answer)