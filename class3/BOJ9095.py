import sys
T = int(sys.stdin.readline())

result = [0] * 11
result[1], result[2], result[3] = 1, 2, 4

for i in range(4, 11):
    result[i] = result[i-1] + result[i-2] + result[i-3]

for tc in range(1, T+1):
    print(result[int(sys.stdin.readline())])