a = input()
alist = list(map(int, a))
temp = False

while alist[0] != 0:
    for i in range(int(len(alist)/2)):
        if alist[i] != alist[-(i+1)]:
            temp = True
    if temp is True:
        print("no")
    else:
        print("yes")
    temp = False
    a = input()
    alist = list(map(int, a))
