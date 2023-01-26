n = int(input())
result = 0

while n >= 2:
    if n % 5 == 0:
        result += 1
        n -= 5
    elif n % 3 == 0:
        result += 1
        n -= 3
    elif n >= 5:
        result += 1
        n -= 5
    else:
        print(-1)
        exit()

print(result)