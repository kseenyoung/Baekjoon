import sys
input = sys.stdin.readline

K, N = map(int, input().split())
numbers = []
maxNum = 0

for i in range(K):
    number = int(input())
    numbers.append(number)

start = 0
end = max(numbers)
while start <= end:
    cnt = 0
    mid = (start + end)//2
    if mid == 0:  # start와 end가 모두 0일 때
        break
    for n in numbers:
        cnt += n//mid

    if cnt >= N:  # 주의 : cnt == N 찾더라도 최대 값을 찾아야 함
        start = mid + 1
    else:
        pass

print(end)
