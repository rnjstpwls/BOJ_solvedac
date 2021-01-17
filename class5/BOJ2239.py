import sys


def back_tracking(idx):
    if idx == length:
        for row in arr:
            print(''.join(row))

        exit()

    cr, cc = blank[idx]
    for num in range(1, 10):
        num = str(num)
        if check_row(cr, num) and check_col(cc, num) and check_box(cr, cc, num):
            arr[cr][cc] = num
            back_tracking(idx + 1)
            arr[cr][cc] = 0





def check_row(row, num):
    for c in range(9):
        if arr[row][c] == num:
            return False
    return True


def check_col(col, num):
    for r in range(9):
        if arr[r][col] == num:
            return False
    return True


def check_box(row, col, num):
    row //= 3
    col //= 3

    for dr in range(3):
        for dc in range(3):
            if arr[3*row + dr][3*col + dc] == num:
                return False
    return True


def check_blank():
    result = []
    for r in range(9):
        for c in range(9):
            if arr[r][c] == '0':
                result.append((r, c))
    return result


sys.stdin = open('input.txt')

input = sys.stdin.readline

arr = list(list(input().strip()) for _ in range(9))

blank = check_blank()
length = len(blank)
back_tracking(0)
