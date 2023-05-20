import sys
input = sys.stdin.readline

def promising(i):
    for k in range(i):
        if row[i] == row[k] or abs(row[i] - row[k]) == i - k:
            return False
    return True
def backtracking(i):
    global result
    if i == N:
        result += 1
        return
    for j in range(N):
        if check[j]:
            continue
        row[i] = j
        if promising(i):
            check[j] = True
            backtracking(i + 1)
            check[j] = False

N = int(input())
row = [0] * N  # board[n] = m은 n행 m열에 퀸을 놓았음을 의미한다
check = [False] * N
result = 0

backtracking(0)

print(result)
