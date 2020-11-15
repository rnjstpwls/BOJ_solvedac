import sys


def binary_search(value):

    if last_value[0] >= value:
        last_value[0] = value
        return
    if last_value[-1] < value:
        last_value.append(value)
        return

    start, end = 0, len(last_value) - 1

    while end-start > 1:
        center = (start + end) // 2
        if last_value[center] == value:
            return
        elif last_value[center] < value:
            start = center
        else:
            end = center
    last_value[end] = value


N = int(sys.stdin.readline())
wires = list(map(int, sys.stdin.readline().split()))

last_value = [float('inf')]

for wire in wires:
    binary_search(wire)
print(len(last_value))

