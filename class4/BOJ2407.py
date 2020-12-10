
n, m = map(int, input().split())

fact = [1]

for i in range(1, n+1):
    fact.append(fact[-1] * i)

print(fact[n] // (fact[m] * fact[n-m]))