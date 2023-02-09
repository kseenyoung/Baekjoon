import sys
input = sys.stdin.readline

N = int(input())
numbers = [0]*10001

for i in range(N):
    number = int(input())
    numbers[number] += 1

for i, n in enumerate(numbers):
    for j in range(n):
        print(i)

