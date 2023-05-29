import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
connected = set()  # 스패닝 트리에 속한 노드
graph = [[] for _ in range(n+1)]  # 각 노드별 연결된 노드들
startNode = (INF, 0)  # (길이, 노드)
result = 0

for _ in range(m):  # 간선
    a, b, w = map(int, input().split())
    # 무방향 그래프이므로 두 노드에 대해서 모두 연결
    graph[a].append((w, b))
    graph[b].append((w, a))
    startNode = (w, a) if startNode[0] > w else startNode  # 가장 작은 간선을 가지는 노드

q = graph[startNode[1]]
heapq.heapify(q)  # 시작 노드에 연결된 모든 노드들 최소 힙 변경

connected.add(startNode[1])  # 시작 노드 연결

while q:
    w, b = heapq.heappop(q)  # 접근 가능한 간선 중 가장 적은 비용
    if b not in connected:  # 연결되지 않았다면
        connected.add(b)  # 노드 연결
        result += w  # 간선 비용 계산

        for w2, a2 in graph[b]:  # 연결된 노드와 연결된 간선들
            if a2 not in connected:  # 이미 연결되어 있지 않다면
                heapq.heappush(q, (w2, a2))  # 최소 힙에 삽입

print(result)