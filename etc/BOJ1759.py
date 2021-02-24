import sys

vowel = ['a', 'e', 'i', 'o', 'u']

def search(idx, j, m, t):
    if idx == C:
        if j+m == L and j >= 2 and m >= 1:
            print(t)
        return
    if j+m > L:
        return



    if text[idx] in vowel:
        search(idx+1, j, m+1, t+text[idx])
    else:
        search(idx+1, j+1, m, t+text[idx])
    search(idx+1, j, m, t)

sys.stdin = open('input.txt')

input = sys.stdin.readline

L, C = map(int, input().split())
text = sorted(input().split())
search(0, 0, 0, '')