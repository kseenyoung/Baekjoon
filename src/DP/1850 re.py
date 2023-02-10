import math
AB = list(map(int, input().split()))
AB.sort(key=lambda x: -x)

while AB[1] != 0:
    AB = [AB[1], AB[0] % AB[1]]

print(AB[0]*"1")