N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))

positive = [0]*10000001
negative = [0]*10000001

for n in numbers:
    if n < 0:
        negative[-n] += 1
    else:
        positive[n] += 1

for c in check:
    if c < 0:
        print(negative[-c], end=" ")
    else:
        print(positive[c], end=" ")