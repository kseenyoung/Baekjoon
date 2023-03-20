
target = int(input())
M = int(input())  # 0 <= M <= 10 , 0일 때 주의
if M != 0:
    brokenButton = list(map(int, input().split()))
else:
    brokenButton = []

result = abs(100 - target)  # +-만 사용

for number in range(1000001):
    number = str(number)  # 포함 되는 숫자 중에 고장난 것이 없는지 확인 하기 위해

    for i, n in enumerate(number):
        if n in brokenButton:  # int 주의
            break
        if i == len(number) - 1:  # number 중 고장난 숫자 없음
            result = min(result, abs(int(number) - target) + len(number))

print(result)
