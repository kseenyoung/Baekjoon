import heapq
INF = int(1e9)

N, K = map(int, input().split())
max_value = max(N, K)
distance = [INF]*100001
def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for a, b in [(now*2, dist), (now+1, dist+1), (now-1, dist+1)]:
            if 0 <= a <= 100000 and distance[a] > b:
                distance[a] = b
                heapq.heappush(q, (b, a))

dijkstra(N)
# print(distance)
print(distance[K])

