target = int(input())
brokenButtonCount = int(input())
if brokenButtonCount == 0:
    print(min(abs(100 - target), len(str(target))))
else:
    brokenButton = list(map(int, input().split()))

    minN = abs(100 - target)  # +/- 만 사용하여 이동한 경우

    for num in range(1000001):  # 채널 제한은 없고 이동하려는 채널 제한은 500,000까지
        num = str(num)

        for i, n in enumerate(num):
            if int(n) in brokenButton:  # 이동하려는 번호 중 망가진 버튼이 있는 경우
                break
            if i == len(num) - 1:  # 마지막 버튼까지 확인 & 문제 없는 경우
                minN = min(minN, len(num) + abs(target - int(num)))  # 지금까지 나온 것 vs (버튼 누름 + 이동)

    print(minN)