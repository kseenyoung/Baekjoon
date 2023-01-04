alist = list(map(int, input().split()))
result = 0

for i in range(5):
    result += alist[i]*alist[i]

print(result % 10)