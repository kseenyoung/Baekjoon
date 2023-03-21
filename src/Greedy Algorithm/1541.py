from collections import deque

num = ''
result = 0
minus = 0
temp = False
string = input()

for s in string:
    if s.isdigit():
        num += s
    else:
        if temp:  # - 있었음
            minus += int(num)
            num = ''
            if s == '-':
                result -= minus
                minus = 0
            # else:
            #     temp = False
        else:  # - 없었음
            result += int(num)
            num = ''
            if s == '-':
                temp = True

# 마지막 숫자 계산
if temp:
    minus += int(num)
    result -= minus
else:
    result += int(num)

print(result)
