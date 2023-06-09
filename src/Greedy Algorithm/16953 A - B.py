from collections import deque
a, b = map(int, input().split())
que = deque()  # BFS

que.append((a*2, 2))  # 2곱하기 연산
que.append((int(str(a)+'1'), 2))  # 1자리수 더하기 연산

while que:  # 큐에 값이 있을 동안
    q = que.popleft()
    if q[0] == b:
        print(q[1])  # 가장 먼저 발견 되는 타겟값 연산 횟수 출력
        exit()  # 종료
    else:
        # 두 개의 연산에 대해 타겟 값보다 작거나 같다면 큐에 삽입
        if q[0]*2 <= b:
            que.append((q[0]*2, q[1]+1))
        if int(str(q[0])+'1') <= b:
            que.append((int(str(q[0])+'1'), q[1]+1))

print(-1)  # 모든 경우의 수에서 타겟 찾지 못 한다면
