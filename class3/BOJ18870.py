import sys


N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
check = sorted(list(set(numbers)))

check_dic = {check[i]: i for i in range(len(check))}
# print(check_dic)

print(*[check_dic[n] for n in numbers])