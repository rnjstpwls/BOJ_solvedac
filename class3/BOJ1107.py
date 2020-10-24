import sys


def ch_check(num):
    for char in str(num):
        if char in btn:
            return False
    return True


input = sys.stdin.readline

N = int(input())
M = int(input())
if M == 0:
    btn = []
else:
    btn = list(input().strip().split())
result = abs(100-N)

for ch in range(0, 1000000 + 1):
    if ch_check(ch):
        result = min(abs(ch-N)+len(str(ch)), result)
print(result)