from itertools import permutations

n = int(input())
alist = list(map(int, input().split()))

maxN = 0
nPr = permutations(alist)
for p in nPr:
    temp = 0
    for i in range(n-1):
        temp += abs(p[i] - p[i+1])
    if temp > maxN:
        maxN = temp

print(maxN)

# def dfs(level):
#     if level == n:
#         print(result)
#     else:
#         for i in range(n):
#             if not visited[i]:
#                 result[level] = alist[i]
#                 visited[i] = True
#                 dfs(level+1)
#                 visited[i] = False
#
# result = [0] * n
# visited = [False] * n
# dfs(0)
