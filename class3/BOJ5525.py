import sys


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = sys.stdin.readline().strip()

result = 0

idx = 1
tmp = 0
while idx < M-1:
    if S[idx-1] == 'I' and S[idx] == 'O' and S[idx+1] == 'I':
        tmp += 1
        if tmp == N:
            tmp -= 1
            result += 1
        idx += 1
    else:
        tmp = 0
    idx += 1



print(result)
