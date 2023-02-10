n = int(input())

alist = [0] * (n + 1)
alist[1:3] = [1, 3]

for i in range(3, n + 1):
    alist[i] = alist[i-1] + alist[i-2]*2
# print(alist)
print(alist[n]%10007)
