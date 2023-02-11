import sys

input = sys.stdin.readline

N, M = map(int, input().split())
vertex = {}
stack = []
visited = set()
result = 0

for i in range(M):
    v1, v2 = map(int, input().split())
    vertex[v1] = vertex.get(v1, []) + [v2]  # get, dic에 사용하는 함수
    vertex[v2] = vertex.get(v2, []) + [v1]

for i in range(1, N+1):
    if i not in visited:
        visited.add(i)
        if i not in vertex:
            result += 1
        else:
            stack.append(i)
            while stack:
                s = stack.pop()
                if s in vertex:
                    for j in vertex[s]:
                        if j not in visited:
                            stack.append(j)
                            visited.add(j)

            result += 1

print(result)