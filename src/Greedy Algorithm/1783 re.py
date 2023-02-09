N, M = map(int, input().split())

if N == 1:
    print(1)
elif N == 2:
    # if N >= 3:
    print(min(4, (M-1)//2 + 1))  # 놓친 부분 #M을 기준 으로,,
    # else:
    #     print(1)
# elif N == 2:  # M >= 3
#     print(min(4, (M-1)//2 + 1))  # 놓친 부분, 괄호 주의
else:  # 모든 조건에 오른쪽 감, 오른쪽 이동 수가 중요. N >= 3
    if M < 7:  # 모든 조건을 만족 못 함. 최대 값을 구한다
        print(min(4, M))  # 1, 4 연속 수행 횟수 vs 4회
    else:  # M >= 7
        print(M - 2)