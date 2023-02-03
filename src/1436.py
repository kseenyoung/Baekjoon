n = int(input())
check = '666'
list666 = []

for num in range(666, 10000000):
   if check in str(num):
      list666.append(num)

print(list666[n-1])