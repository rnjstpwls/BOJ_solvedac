import sys
import bisect

def binary_search(s, e, v):

    index = bisect.bisect(end_time, s) - 1
    dp[e] = max(dp[end_time[index]] + v, dp[end_time[-1]])
    end_time.append(e)
    return


sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())

meeting = [tuple(map(int, input().split())) for _ in range(N)]

meeting.sort(key=lambda x:x[1])

end_time = [0]
dp = dict()
dp[0] = 0

for s, e, v in meeting:
    binary_search(s, e, v)

print(dp[end_time[-1]])