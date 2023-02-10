M = int(input())
N = int(input())

alist = []

for i in range(M, N+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:  #break없이 빠져 나왔을 때 for-else
        alist.append(i)

if 1 in alist:
    alist.pop(0)

if alist:
    print(sum(alist))
    print(alist[0])
else:
    print(-1)