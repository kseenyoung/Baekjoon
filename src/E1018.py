n, m = list(map(int, input().split()))
# board = [[0]*m for i in range(n)]
board = [] # 초기화 하지 않아도 됨
result = []

#board 읽기
for i in range(n):
    # board[i] = list(input())
    board.append(input())

for a in range(n-7): # -8 -> -7
    for b in range(m-7):
        result1 = 0
        result2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0: #B로 시작 하는 경우
                    if board[i][j] != 'B':
                        result1 += 1
                    if board[i][j] != 'W':
                        result2 += 1
                else: #W로 시작 하는 경우
                    if board[i][j] != 'W':
                        result1 += 1
                    if board[i][j] != 'B':
                        result2 += 1

        #B(result1)또는 W(result2)로 시작 경우중 작은 것 대입
        result.append(min(result1, result2))

#입력 된 모든 값 중 가장 작은 값 출력
print(min(result))
