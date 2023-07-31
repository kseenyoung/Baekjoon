import sys
import heapq
input = sys.stdin.readline

n = int(input())
graph = []
temp = [[False]*n for _ in range(n)]
result = 1e9
for _ in range(n):
    graph.append(list(map(int, input().split())))

q = []
heapq.heappush(q, (0, 0, 0))  # (비용, row, column)

while q:
    w, row, col = heapq.heappop(q)
    temp[row][col] = True
    if row == n-1 and col == n-1:
        result = min(result, w)
    else:
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            r = row + dr
            c = col + dc
            if -1 < r < n and -1 < c < n and not temp[r][c]:
                cost = w + (graph[r][c] - graph[row][col] if graph[r][c] - graph[row][col] > 0 else 0)
                temp[r][c] = True
                heapq.heappush(q, (cost, r, c))
                print(q)

print(result)
