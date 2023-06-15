import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
answer = [0]*k
edges = []
que = []
connected = set()

for i in range(m):
    a, b = map(int, input().split())
    edges.append((i+1, a, b))

parent = [i for i in range(n+1)]
def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    min_value = min(a, b)
    max_value = max(a, b)
    parent[max_value] = min_value

for i in range(k):
    result = 0
    parent = [i for i in range(n + 1)]

    for j in range(m-i):
        w, a, b = edges[j]
        if find_parent(a) != find_parent(b):
            connected.add((a, b))
            union(a, b)
            result += w

    if len(connected) != n-1:
        break

    answer[i] = result
    edges.pop(0)
    connected = set()
    connected.add((edges[0][1], edges[0][2]))

for i in range(k):
    print(answer[i], end=" ")
