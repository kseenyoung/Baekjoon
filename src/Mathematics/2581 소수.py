M = int(input())
N = int(input())
result = []

for i in range(M, N + 1):
    temp = False
    for j in range(2, i):
        if i % j == 0:
            temp = True
            break
    if not temp:
        if i != 1:  # [주의]1은 소수가 아니다
            result.append(i)

if result:
    print(sum(result))
    print(min(result))
else:
    print(-1)
