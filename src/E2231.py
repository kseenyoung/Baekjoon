alist = [0]*1000000
userN = int(input())

for i in range(1000000):
    num = i
    while int(num) != 0:  #int()
        alist[i] += int(num % 10)
        num /= 10
    alist[i] += i

for i in range(1000000):
    if userN == alist[i]:
        print(i)
        exit()
print(0)