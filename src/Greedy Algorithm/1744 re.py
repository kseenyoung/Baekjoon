import sys

input = sys.stdin.readline

n = int(input())
positive = []
negative = []
result = 0
for i in range(n):
    number = int(input())
    if number == 1:
        result += 1
    elif number <= 0:
        negative.append(number)
    else:  # 양수
        positive.append(number)

positive.sort(key=lambda x: -x)
negative.sort()

i = 0
while i < len(positive):
    if i == len(positive)-1:
        result += positive[-1]
        break
    result += positive[i] * positive[i+1]
    i += 2

i = 0
while i < len(negative):
    if i == len(negative)-1:
        result += negative[-1]
        break
    result += negative[i] * negative[i+1]
    i += 2



print(result)