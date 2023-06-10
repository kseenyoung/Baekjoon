from collections import deque
N = int(input())
cards = [i for i in range(1, N+1)]
que = deque(cards)

while len(que) != 1:
    que.popleft()
    que.append(que.popleft())

print(que[0])
