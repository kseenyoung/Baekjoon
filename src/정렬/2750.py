from sys import stdin
n = int(stdin.readline())
alist = []

for _ in range(n):
    alist.append(int(stdin.readline()))

alist.sort()
for i in alist:
    print(i)
