import sys
input = sys.stdin.readline
V, E = map(int, input().split())
edges = []

for i in range(E):
    a, b, w = map(int, input().split())
    edges.append((w, a, b))

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(V+1)]
edges.sort()
result = 0

for w, a, b in edges:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += w

print(result)