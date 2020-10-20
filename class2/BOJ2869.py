import sys
A, B, V = map(int, sys.stdin.readline().split())

if A >= V:
    print(1)
    exit()

hegith = A
day = 1
plus = A-B
day += ((V-A) // plus)
if (V-A)%(A-B):
    print(day+1)
else:
    print(day)