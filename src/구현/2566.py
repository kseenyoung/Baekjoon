import sys
input = sys.stdin.readline

maxN = 0
position = [0, 0]

for i in range(9):
    line = list(map(int, input().split()))
    maxTemp = max(line)
    if maxTemp > maxN:
        maxN = maxTemp
        position = [i, line.index(maxTemp)]

print(maxN)
print(position[0]+1, position[1]+1)