import sys

input = sys.stdin.readline

N, r, c = map(int, input().split())

start_row, start_col = 0, 0
end_row, end_col = 2**N - 1, 2**N - 1
start, end = 0, (2**N)**2 - 1

while start != end:
    center_row = (start_row + end_row) // 2
    center_col = (start_col + end_col) // 2

    if r <= center_row:
        end_row = center_row
        end = (start + end) // 2
    else:
        start_row = center_row + 1
        start = (start + end) // 2 + 1

    if c <= center_col:
        end_col = center_col
        end = (start + end) // 2
    else:
        start_col = center_col + 1
        start = (start + end) // 2 + 1

print(start)
