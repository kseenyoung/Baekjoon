import sys
input = sys.stdin.readline

T = int(input())  # test case
alist = [[1, 0], [0, 1]] + [[0, 0] for _ in range(39)]  # 0 ~ 40까지 [0이 불린 횟수, 1이 불린 횟수]

for i in range(2, 41):  # i >= 2일 때, a(i) = a(i-1) + a(i-2) 점화식
    alist[i][0] = alist[i-2][0] + alist[i-1][0]
    alist[i][1] = alist[i-2][1] + alist[i-1][1]

for _ in range(T):
    n = int(input())  # 각 요청에 따라 결과값 출력
    print(alist[n][0], alist[n][1])
