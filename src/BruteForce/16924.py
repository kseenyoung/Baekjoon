import sys
import copy

input = sys.stdin.readline

N, M = map(int, input().split())
board = []
result = []
for _ in range(N):
    line = list(input().strip())
    board.append(line)

tempBoard = copy.deepcopy(board)

for i in range(1, N):
    for j in range(1, M):  # 한 칸씩 이동
        if board[i][j] == '*':  # 십자가의 중심일지도 모르는 위치
            up = down = i
            left = right = j
            size = 0
            while True:
                up -= 1
                down += 1
                left -= 1
                right += 1
                if up >= 0 and down < N and left >= 0 and right < M and board[up][j] == '*' and board[down][j] == '*' and board[i][left] == '*' and board[i][right] == '*':
                    size += 1
                    tempBoard[up][j] = tempBoard[down][j] = tempBoard[i][left] = tempBoard[i][right] = '.'
                    result.append((i+1, j+1, size))
                else:  # 더이상 십자가 없음. 현재 크기 입력
                    if size > 0:
                        tempBoard[i][j] = '.'
                    break

temp = True
for t in tempBoard:
    if '*' in t:
        print(-1)
        temp = False
        break

if temp:
    result.sort(key=lambda x: (x[0], x[1], -x[2]))
    print(len(result))
    for r in result:
        print(r[0], r[1], r[2])





