import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())

dp_lefted_min, dp_centered_min, dp_righted_min = map(int, input().split())
dp_lefted_max, dp_centered_max, dp_righted_max = dp_lefted_min, dp_centered_min, dp_righted_min

for _ in range(N-1):
    left, center, right = map(int, input().split())
    dp_left_min = left + min(dp_lefted_min, dp_centered_min)
    dp_center_min = center + min(dp_lefted_min, dp_centered_min, dp_righted_min)
    dp_right_min = right + min(dp_centered_min, dp_righted_min)

    dp_left_max = left + max(dp_lefted_max, dp_centered_max)
    dp_center_max = center + max(dp_lefted_max, dp_centered_max, dp_righted_max)
    dp_right_max = right + max(dp_centered_max, dp_righted_max)
    dp_lefted_min, dp_centered_min, dp_righted_min = dp_left_min, dp_center_min, dp_right_min
    dp_lefted_max, dp_centered_max, dp_righted_max = dp_left_max, dp_center_max, dp_right_max

print(max(dp_lefted_max, dp_centered_max, dp_righted_max), min(dp_lefted_min, dp_centered_min, dp_righted_min))

