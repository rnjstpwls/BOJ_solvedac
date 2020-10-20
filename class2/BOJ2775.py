import sys
T = int(sys.stdin.readline())

apartment = [[0]*15 for _ in range(15)]
for i in range(1,15):
    apartment[0][i] = i

for i in range(1,15):
    for j in range(1,15):
        apartment[i][j] = sum(apartment[i-1][0:j+1])

for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(apartment[k][n])