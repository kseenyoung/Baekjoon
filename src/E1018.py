n, m = list(map(int, input().split()))
board = [['']*n for i in range(m)]
result = 0
minN = 0

for i in range(n):
    board[i] = list(input())

for i in range(8):
    for j in range(8):
        if board[i][j] == 'B':
            result -= 1
        else:
            result += 1
minN = int(abs(result) / 2)

for n in range(n-8):
    for m in range(m-8):

        for i in range(n, n+8):
            for j in range(m, m+8):
                if board[i][j] == 'B':
                    result -= 1
                else:
                    result += 1
        if int(abs(result)/2) < minN:
            minN = int(abs(result)/2)
        result = 0

print(minN)

