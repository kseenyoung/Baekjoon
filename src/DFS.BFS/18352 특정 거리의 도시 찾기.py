import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [INF]*(N+1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + 1
            if distance[i] > cost:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

dijkstra(X)
flag = False
for i in range(1, N+1):
    if K == distance[i]:
        print(i)
        flag = True

if not flag:
    print(-1)