from collections import deque
import sys
input = sys.stdin.readline

dr = [1, -1, 0, 0]  # down, up, right, left
dc = [0, 0, 1, -1]

N, K = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

S, X, Y = map(int, input().split())

q = []
for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            q.append((board[i][j], i, j, 0))
q.sort()  # (주의) 리스트로 받아 정렬 후 queue로 변경!
q = deque(q)

while q:
    viru, row, col, time = q.popleft()
    if time == S:
        break
    for d in range(4):
        r = row + dr[d]
        c = col + dc[d]
        if -1 < r < N and -1 < c < N and not board[r][c]:  # 범위를 벗어나지 않고 위치 값이 0일 때
            board[r][c] = viru
            q.append((viru, r, c, time+1))

# for i in range(N):
#     print(board[i])

print(board[X-1][Y-1])
