# pypy

N = int(input())
numbers = [4] * (N+1)

for i in range(1, int(N**0.5)+1):
    numbers[i*i] = 1

for i in range(2, N+1):
    for j in range(1, int(i**0.5)+1):
        numbers[i] = min(numbers[i], numbers[i-j*j]+1)
print(numbers[N])