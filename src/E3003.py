num_list = list(map(int, input().split()))
num = 0

while num_list[0] != 1:
    if num_list[0] > 1:
        num_list[0] -= 1
        num -= 1
    else:
        num_list[0] += 1
        num += 1
print(num)
num = 0

while num_list[1] != 1:
    if num_list[1] > 1:
        num_list[1] -= 1
        num -= 1
    else:
        num_list[1] += 1
        num += 1
print(num)
num = 0

while num_list[2] != 2:
    if num_list[2] > 2:
        num_list[2] -= 1
        num -= 1
    else:
        num_list[2] += 1
        num += 1
print(num)
num = 0

while num_list[3] != 2:
    if num_list[3] > 2:
        num_list[3] -= 1
        num -= 1
    else:
        num_list[3] += 1
        num += 1
print(num)
num = 0

while num_list[4] != 2:
    if num_list[4] > 2:
        num_list[4] -= 1
        num -= 1
    else:
        num_list[4] += 1
        num += 1
print(num)
num = 0

while num_list[5] != 8:
    if num_list[5] > 8:
        num_list[5] -= 1
        num -= 1
    else:
        num_list[5] += 1
        num += 1
print(num)
