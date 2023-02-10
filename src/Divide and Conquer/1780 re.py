import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())
board = []
result = [0, 0, 0]

for i in range(N):  # 9로 고정 시켜 놓고 틀린 부분 찾고 있었음,,
    line = list(map(int, input().split()))
    board.append(line)


def loop(r, c, volume):
    checkNum = board[r][c]
    if volume == 1:
        result[checkNum] += 1
        return

    for i in range(r, r + volume):
        for j in range(c, c + volume):
            if board[i][j] != checkNum:

                for k in range(3):
                    for l in range(3):
                        loop(r + k * volume // 3, c + l * volume // 3, volume // 3)
                return

    result[checkNum] += 1
    return


loop(0, 0, N)

print(result[-1])
print(result[0])
print(result[1])
