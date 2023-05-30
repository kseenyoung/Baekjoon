n = int(input())
numbers = set()
for i in list(map(int, input().split())):
    numbers.add(i)
m = int(input())
numbers2 = list(map(int, input().split()))

for i in numbers2:
    print(1 if i in numbers else 0)