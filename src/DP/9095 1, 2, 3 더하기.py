import sys
input = sys.stdin.readline

# 각 인덱스 값을 만들 수 있는 개수 저장
# 1은 1개, 2는 2개, 3은 4개의 만들 수 있는 조합이 존재 함
numbers = [0, 1, 2, 4] + [0]*7
n = int(input())

for i in range(4, 11):
    numbers[i] = numbers[i-3] + numbers[i-2] + numbers[i-1]  # 점화식

# print(numbers)   # [0, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274]

for i in range(n):
    m = int(input())  # 각 요구 값의 (만들 수 있는) 개수 반환
    print(numbers[m])

