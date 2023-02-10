import sys

input = sys.stdin.readline

n = int(input())
meeting = []

for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))

meeting.sort(key=lambda x: (x[1], x[0]))

result = 0
current = 0
for m in meeting:
    if current <= m[0]:
        result += 1
        current = m[1]

print(result)
