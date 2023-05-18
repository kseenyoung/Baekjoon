import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance2 = [INF]*(N+1)
distance3 = [INF]*(N+1)

for _ in range(E):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))
v1, v2 = map(int, input().split())

def dijkstra(start, distance):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for v, w in graph[now]:
            cost = dist + w
            if distance[v] > cost:
                distance[v] = cost
                heapq.heappush(q, (cost, v))


# dijkstra(1, distance1)
dijkstra(v1, distance2)
dijkstra(v2, distance3)

print(distance2)
print(distance3)

result = min(distance2[1] + distance3[N] + distance2[v2], distance3[1] + distance2[N] + distance3[v1])

print(-1 if result >= INF else result)