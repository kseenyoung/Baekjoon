import sys

input = sys.stdin.readline
numbers = {}
n = int(input())

for i in range(n):
    number = int(input())
    if number not in numbers:
        numbers[number] = 1
    else:
        numbers[number] += 1

sortedD = sorted(numbers, key=lambda x: (-numbers[x], x))

print(sortedD[0])