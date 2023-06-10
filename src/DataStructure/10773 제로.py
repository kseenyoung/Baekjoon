from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
numbers = []
que = deque()
result = 0

for _ in range(n):
    a = int(input())
    if a == 0:
        result -= numbers.pop()
    else:
        numbers.append(a)
        result += a

print(result)