import sys
N = int(sys.stdin.readline())
user = [[] for _ in range(201)]

for _ in range(N):
    age, name = sys.stdin.readline().split()
    user[int(age)].append(f'{age} {name}')

for u in user:
    if u:
        for i in u:
            print(i)