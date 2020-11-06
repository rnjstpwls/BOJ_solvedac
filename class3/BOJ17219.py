import sys

input = sys.stdin.readline

N, M = map(int, input().split())
password = dict()
for _ in range(N):
    address, pw = input().split()
    password[address] = pw

for _ in range(M):
    print(password[input().strip()])