# 미완(시간 초과)
import sys
sys.setrecursionlimit(100000)

N = int(input())
row = [0]*N
result = 0

def promising(i):
    for j in range(i):
        if row[i] == row[j] or abs(row[i] - row[j]) == abs(i - j):
            return False
    return True


def backtracking(i):
    global result
    if i == N:
        for j in range(N):
            print(row[j]+1)
        exit()
    for j in range(N):
        row[i] = j
        if promising(i):
            backtracking(i+1)



backtracking(0)
