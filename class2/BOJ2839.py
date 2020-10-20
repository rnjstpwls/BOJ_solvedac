import sys

sugar = [0] * 5001
sugar[3], sugar[5] = 1, 1
for i in range(6, 5001):
    if not sugar[i-3] and not sugar[i-5]:
        continue
    elif sugar[i-3] and not sugar[i-5]:
        sugar[i] = sugar[i-3] + 1
    elif not sugar[i-3] and sugar[i-5]:
        sugar[i] = sugar[i-5] + 1
    else:
        sugar[i] = min(sugar[i-3], sugar[i-5]) + 1

N = int(sys.stdin.readline())
if sugar[N]:
    print(sugar[N])
else:
    print(-1)