num = list(map(int, input().split()))
row = num[0]
col = num[1]

A = [[0]*col for i in range(row)]

for n in range(row):
    templist = list(map(int, input().split()))
    for nn in range(col):
        A[n][nn] = templist[nn]

for n in range(row):
    templist = list(map(int, input().split()))
    for nn in range(col):
        A[n][nn] = templist[nn] + A[n][nn]

for r in range(row):
    for c in range(col):
        print(A[r][c], end= " ")
    print("")