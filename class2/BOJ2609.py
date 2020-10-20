import sys
N, M = map(int, sys.stdin.readline().split())
N_instance = []
M_instance = []
for i in range(1, int(N**0.5)+1):
    if N % i == 0:
        N_instance.append(i)
        N_instance.append(N//i)
for i in range(1, int(M**0.5)+1):
    if M % i == 0:
        M_instance.append(i)
        M_instance.append(M//i)
N_instance = set(N_instance)
M_instance = set(M_instance)
LCD = max(N_instance&M_instance)
print(LCD)
print(N*M//LCD)

