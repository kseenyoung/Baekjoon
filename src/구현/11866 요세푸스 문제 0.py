from collections import deque

N, K = map(int, input().split())

# 풀이2(100%)
que = deque()
index = K
for i in range(1, N+1):
    que.append(i)

print("<", end="")
while len(que) != 1:
    q = que.popleft()
    index -= 1
    if index == 0:
        print(str(q) + ", ", end="")
        index = K
    else:
        que.append(q)
print(str(que[0]) + ">")

# 풀이1(96%, 시간초과)

# numbers = [False]*(N+1)
#
# q = K
# numbers[K] = True
# answer = 1
#
# print("<" + str(K) + ", ", end="")
# while True:
#     tempK = K
#     while tempK != 0:
#         q = (q+1) % (N+1)
#         q += 1 if q == 0 else 0  # q가 0이라면 1로 변경
#         if not numbers[q]:
#             tempK -= 1
#     if not numbers[q]:
#         numbers[q] = True
#         answer += 1
#         if answer == N:
#             print(str(q) + ">")
#             break
#         else:
#             print(str(q) + ", ", end="")
