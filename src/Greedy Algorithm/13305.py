N = int(input())
edges = list(map(int, input().split()))
vertex = list(map(int, input().split()))

# 내 풀이
# charge = 0  # 총 지불 금액
# distance = sum(edges)  # 남은 거리
# position = 0  # 현재 위치
# i = 0
#
# while distance:
#     j = i  # 현재 위치
#     while i < len(vertex)-1 and vertex[i] < vertex[i+1]:
#         distance -= edges[i]
#         charge += vertex[j] * edges[i]
#         i += 1
#         if distance == 0:
#             break
#     else:
#         if i == len(vertex)-1:
#             distance -= edges[i-1]
#             charge += vertex[j] * edges[i-1]
#         else:
#             distance -= edges[i]
#             charge += vertex[j] * edges[i]
#             i += 1
#
# print(charge)

# 풀이 참고
result = 0
minCharge = vertex[0]
distance = edges[0]

for i in range(N-1):
    if minCharge > vertex[i]:
        minCharge = vertex[i]
    result += minCharge * edges[i]

print(result)
