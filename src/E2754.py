score = input()

if score[0] == 'F':
    print(0.0)
    exit()

if score[0] == 'A':
    result = 4
elif score[0] == 'B':
    result = 3
elif score[0] == 'C':
    result = 2
elif score[0] == 'D':
    result = 1

if score[1] == '+':
    result += 0.3
elif score[1] == '0':
    result += 0.0
elif score[1] == '-':
    result -= 1
    result += 0.7

print(result)