result = 'm'
alist = list(map(int, input().split()))

if alist[0] == 1:
    result = 'a'
elif alist[0] == 8:
    result = 'd'

for i in range(8):
    if result == 'a' and alist[i] != i + 1:
        result = 'm'
        break
    elif result == 'd' and alist[i] != 8 - i:
        result = 'm'
    if result == 'm':
        break

if result == 'a':
    print("ascending")
elif result == 'd':
    print("descending")
else:
    print("mixed")
