from collections import deque
import bisect
import sys

input = sys.stdin.readline


T = int(input())

for _ in range(T):
    k = int(input())
    q = deque()
    q_dic = dict()
    for _ in range(k):
        command, value = input().split()
        value = int(value)
        if command == 'I':
            try:
                q_dic[value] += 1
            except:
                q_dic[value] = 1
                bisect.insort(q, value)
        else:
            if not q:
                continue
            if value == 1:
                if q_dic[q[-1]] == 1:
                    q_dic.pop(q.pop())
                else:
                    q_dic[q[-1]] -= 1
            else:
                if q_dic[q[0]] == 1:
                    q_dic.pop(q.popleft())
                else:
                    q_dic[q[0]] -= 1

    if q:
        print(q[-1], q[0])
    else:
        print('EMPTY')
