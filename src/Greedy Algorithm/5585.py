charge = [500, 100, 50, 10, 5, 1]

money = 1000 - int(input())
result = 0

for c in charge:
    result += money // c
    money %= c

print(result)