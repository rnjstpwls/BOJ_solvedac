import sys



N = int(sys.stdin.readline())

numbers = []
for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()

print(round(sum(numbers) / N))
print(numbers[N//2])


num_count = [0] * 8001
for n in numbers:
    num_count[n+4000] += 1
result = max(num_count)
cnt = 0
for i in range(8001):
    if num_count[i] == result:
        cnt += 1
        if cnt == 2:
            print(i-4000)
            break
else:
    print(num_count.index(result)-4000)


print(numbers[-1]-numbers[0])