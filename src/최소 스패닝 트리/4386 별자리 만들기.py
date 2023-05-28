import math
import sys
input = sys.stdin.readline

n = int(input())
alist = []
edges = []
parent = [i for i in range(n+1)]
for _ in range(n):
    x, y = map(float, input().split())
    alist.append((x, y))

for i in range(n):
    for j in range(i+1, n):
        x1, y1 = alist[i]
        x2, y2 = alist[j]
        edges.append((math.sqrt((x1 - x2)**2 + (y1 - y2)**2), i, j))

edges.sort()

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

result = 0
for w, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        result += w

print(round(result, 2))