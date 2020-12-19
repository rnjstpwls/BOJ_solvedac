# pypy

def search(row):
    global result
    if row == N:
        result += 1
        return

    for col in range(N):
        if not column[col] and not slash[row + col] and not back_slash[col - row + N - 1]:
            column[col] = slash[row + col] = back_slash[col - row + N - 1] = True
            search(row+1)
            column[col] = slash[row + col] = back_slash[col - row + N - 1] = False


N = int(input())

column = [False] * N
# row + col
slash = [False] * (2 * N - 1)
# col - row + N - 1
back_slash = [False] * (2 * N - 1)

result = 0
search(0)
print(result)
