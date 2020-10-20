import sys

# r = 31 // M = 1234567891
L = int(sys.stdin.readline())
txt = sys.stdin.readline().strip()
# print(txt)

# print(ord('a')) // 97
# print(ord('z')) // 122
total = 0
for i in range(len(txt)):
    total += ((ord(txt[i])-96) * (31 ** i))
print(total%1234567891)