import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    numbers = list(input().strip() for _ in range(N))
    numbers.sort(key=lambda x: len(x))
    registered = set()
    result = 'YES'
    for number in numbers:
        length = len(number)
        string = ''
        for i in range(length):
            string += number[i]
            if string in registered:
                result = 'NO'
                break
        else:
            registered.add(number)
            continue
        break
    print(result)