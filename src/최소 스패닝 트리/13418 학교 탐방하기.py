import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
graph2 = [[] for _ in range(n+1)]
connected = set()

a, b, w = map(int, input().split())
flag, flag2 = w, w
graph[0].append((w, 1))  # 0과 1 간선

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((w, b))
    graph[b].append((w, a))
    graph2[a].append((-w, b))
    graph2[b].append((-w, a))

edges = graph[0]
heapq.heapify(edges)
connected.add(0)
result = 0

while edges:
    w1, v1 = heapq.heappop(edges)
    if v1 not in connected:
        connected.add(v1)
        if w1:
            flag = 1
            result += 1
        else:
            flag = 0
        for w2, v2 in graph[v1]:
            if v2 not in connected:
                heapq.heappush(edges, (w2, v2))

minValue = result**2

connected = set()
graph2[0].append((-flag2, 1))  # 0과 1 간선

edges = graph2[0]
heapq.heapify(edges)
connected.add(0)
result = 0

while edges:
    w1, v1 = heapq.heappop(edges)
    if v1 not in connected:
        connected.add(v1)
        if w1:
            flag2 = 1
            result += 1
        else:
            flag2 = 0
        for w2, v2 in graph2[v1]:
            if v2 not in connected:
                heapq.heappush(edges, (w2, v2))

maxValue = result**2
print(maxValue - minValue)