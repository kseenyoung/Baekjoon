import sys
input = sys.stdin.readline

n = int(input())
edges = []  # 비용 오름차순을 위한 리스트
parent = [i for i in range(n+1)]  # 서로소 집합 (본인을 부모로 갖도록 초기화)

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(i+1, n):  # 인접 행렬이 대칭을 이므로 i+1부터 n까지 정보만 알면 됨
        edges.append((temp[j], i, j))

edges.sort()  # 비용 기준으로 오름차순

def find_parent(x):  # 부모 노드 찾기
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):  # 부모 노드 합치기
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

result = 0

for w, a, b in edges:
    if find_parent(a) != find_parent(b):  # 사이클이 생기지 않는다면
        union_parent(a, b)  # 같은 부모(집합)으로
        result += w  # 비용 계산

print(result)
