total = int(input())
count = int(input())
sum = 0

for num in range(0, count):
    item = list(map(int, input().split()))
    sum += (item[0] * item[1])

if sum == total:
    print("Yes")
else:
    print("No")