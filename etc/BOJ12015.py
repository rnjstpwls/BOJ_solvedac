import sys

def search(num):

    if num <= memory[0]:
        memory[0] = num
        return
    if memory[-1] < num:
        memory.append(num)
        return

    start, end = 0, len(memory) - 1

    while start <= end:
        center = (start+end)//2
        if memory[center] == num:
            return
        elif memory[center] < num:
            start = center + 1
        else:
            end = center - 1
    memory[start] = num

sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
memory = [sys.maxsize]

for num in A:
    search(num)
print(len(memory))