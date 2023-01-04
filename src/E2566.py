maxN = 0
row = 1
col = 1

for i in range(9):
    nlist = list(map(int, input().split()))
    if max(nlist) > maxN:
        maxN = max(nlist)
        row = i + 1
        col = nlist.index(maxN) + 1

print(maxN)
print(row, col)
