nlist = [0 for i in range(30)]

for n in range(0, 28):
    num = int(input())
    nlist[num-1] = 1

for n in range(0, 30):
    if nlist[n] == 0:
        print(n+1)