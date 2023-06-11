from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    que = deque()
    for i in range(N):
        que.append((numbers[i], i))

    no = 1
    numbers.sort(reverse=True)

    while que:
        q = que.popleft()
        if q[0] == numbers[no-1]:
            if q[1] == M:
                print(no)
                break
            no += 1
        else:
            que.append(q)
