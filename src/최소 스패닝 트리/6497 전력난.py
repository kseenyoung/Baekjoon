import sys
input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    minP, maxP = min(a, b), max(a, b)
    parent[maxP] = minP


while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    edges = []
    parent = [i for i in range(m)]
    result = 0

    for _ in range(n):
        x, y, z = map(int, input().split())
        edges.append((z, x, y))
        result += z

    edges.sort()

    for w, x, y in edges:
        if find(x) != find(y):
            union(x, y)
            result -= w

    print(result)
