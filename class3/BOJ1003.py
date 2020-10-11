import sys

count0 = [1, 0]
count1 = [0, 1]
for i in range(40):
    count0.append(count0[-1] + count0[-2])
    count1.append(count1[-1] + count1[-2])

T = int(sys.stdin.readline())

for _ in range(T):
    tmp = int(sys.stdin.readline())
    print(count0[tmp], count1[tmp])