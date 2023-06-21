import heapq
INF = int(1e9)
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # right, left, down, up

n, m = map(int, input().split())
graph = []
distance = [[INF]*n for _ in range(m)]

for _ in range(m):
    graph.append(input())

que = []
distance[0][0] = 0
heapq.heappush(que, (0, 0, 0))

while que:
    dist, r, c = heapq.heappop(que)
    if distance[r][c] < dist:
        continue
    for dr, dc in directions:
        row = r + dr
        col = c + dc
        if -1 < row < m and -1 < col < n and distance[row][col] > dist + int(graph[row][col]):
            distance[row][col] = dist + int(graph[row][col])
            heapq.heappush(que, (distance[row][col], row, col))

print(distance[m-1][n-1])
