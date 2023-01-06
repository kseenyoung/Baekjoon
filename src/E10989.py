import sys
input = sys.stdin.readline
n = int(input())
alist = [0]*10001

for i in range(n):
    a = int(input())
    alist[a] += 1

for i in range(len(alist)):
    for j in range(alist[i]):
        print(i)
