import sys
input = sys.stdin.readline

n, m = map(int, input().split())
school = [''] + list(input().split())
parent = [i for i in range(n+1)]
edges = []
result = 0

for _ in range(m):
    u, v, d = map(int, input().split())
    edges.append((d, u, v))

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

for w, a, b in edges:
    if find(a) != find(b) and school[a] != school[b]:  # 사이클 발생하지 않고, 여초/ 남초로 다르다면
        union(a, b)
        result += w

print(result if len([i for i in range(1, n+1) if parent[i] == i]) == 1 else -1)
