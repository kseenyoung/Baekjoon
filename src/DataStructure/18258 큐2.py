from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
que = deque()

for _ in range(n):
    alist = list(input().split())
    if alist[0] == 'push':
        que.append(alist[1])
    elif alist[0] == 'front':
        print(que[0] if len(que) != 0 else -1)
    elif alist[0] == 'back':
        if len(que) != 0:
            print(que[-1])
            continue
        print(-1)
    elif alist[0] == 'size':
        print(len(que))
    elif alist[0] == 'pop':
        if len(que) != 0:
            print(que.popleft())
            continue
        print(-1)
    elif alist[0] == 'empty':
        print(0 if len(que) else 1)

