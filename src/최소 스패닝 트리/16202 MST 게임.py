import sys
import heapq
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
connected = set()
que = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((i+1, b))
    graph[b].append((i+1, a))
    if i == 0:
        startNode = a

que = graph[startNode]
heapq.heapify(que)
connected.add(startNode)

result = 0
while que:
    w, b = heapq.heappop(que)
    if b not in connected:
        connected.add(b)
        result += w

        for w2, a2 in graph[b]:
            if a2 not in connected:
                heapq.heappush(que, (w2, a2))

print(result)