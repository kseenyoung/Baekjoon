input()
nlist = list(map(int, input().split()))
v = int(input())
count = 0
for n in nlist:
    if v == n:
        count += 1

print(count)