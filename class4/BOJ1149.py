import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())

RED = [0] * N
GREEN = [0] * N
BLUE = [0] * N

R, G, B = map(int, input().split())
RED[0], GREEN[0], BLUE[0] = R, G, B


for i in range(1, N):
    R, G, B = map(int, input().split())
    RED[i] = R + min(GREEN[i-1], BLUE[i-1])
    GREEN[i] = G + min(RED[i-1], BLUE[i-1])
    BLUE[i] = B + min(RED[i-1], GREEN[i-1])
print(min(RED[-1], GREEN[-1], BLUE[-1]))