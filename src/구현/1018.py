import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [[] for _ in range(N)]  # 행은 for문 열이 *
minN = 64

for i in range(N):
    line = input().rstrip()
    for l in line:
        board[i].append(l)

for i in range(N - 7):
    for j in range(M - 7):
        startB, startW = 0, 0

        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:  # 시작색 같아야 할 위치
                    if board[k][l] == 'B':
                        startW += 1
                    else:
                        startB += 1
                else:  # 시작색 달라야 할 위치
                    if board[k][l] == 'B':
                        startB += 1
                    else:
                        startW += 1
        if minN > min(startB, startW):
            minN = min(startB, startW)

print(minN)