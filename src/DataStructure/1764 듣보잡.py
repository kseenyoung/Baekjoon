N, M = map(int, input().split())
dic = {}
answer = []
for i in range(N):
    name = input()
    if name in dic:
        answer.append(name)
    else:
        dic[name] = 1

for i in range(M):
    name = input()
    if name in dic:
        answer.append(name)
    else:
        dic[name] = 1

print(len(answer))
answer.sort()
for name in answer:
    print(name)