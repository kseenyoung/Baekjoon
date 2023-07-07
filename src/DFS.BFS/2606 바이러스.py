N = int(input())
M = int(input())

graph = [[] for i in range(N+1)]
checked = [False]*(N+1)
answer = 0

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(v):
    global answer
    if not checked[v]:
        checked[v] = True
        answer += 1
        for i in graph[v]:
            dfs(i)


dfs(1)
print(answer-1)
