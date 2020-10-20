import sys
from collections import deque
N = int(sys.stdin.readline())

numbers = deque(range(1,N+1))
while len(numbers) > 1:
    drop = numbers.popleft()
    top = numbers.popleft()
    numbers.append(top)

print(numbers[0])
