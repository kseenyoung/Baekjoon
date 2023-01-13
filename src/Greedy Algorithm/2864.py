a, b = input().split()
minN, maxN = 0, 0

#a와 b의 6을 모두 5로 전환
a5 = ['5' if i == '6' else i for i in a]
b5 = ['5' if i == '6' else i for i in b]

for i, n in enumerate(a5):
    if i == len(a5)-1:
        minN += int(n)
        break
    minN += 10 ** (len(a5) - i - 1) * int(n)
for i, n in enumerate(b5):
    if i == len(b5)-1:
        minN += int(n)
        break
    minN += 10 ** (len(b5) - i - 1) * int(n)

print(minN, end=" ")

a6 = ['6' if i == '5' else i for i in a5]
b6 = ['6' if i == '5' else i for i in b5]

for i, n in enumerate(a6):
    if i == len(a6)-1:
        maxN += int(n)
        break
    maxN += 10 ** (len(a6) - i - 1) * int(n)
for i, n in enumerate(b6):
    if i == len(b6)-1:
        maxN += int(n)
        break
    maxN += 10 ** (len(b6) - i - 1) * int(n)

print(maxN)
