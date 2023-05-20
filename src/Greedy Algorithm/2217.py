import sys

input = sys.stdin.readline

N = int(input())
rope = []

for _ in range(N):
    rope.append(int(input()))
rope.sort(reverse=True)

w = 0
countRope = 0
result = []

for r in rope:
    countRope += 1
    temp = w // countRope  # rope 당 감당할 무게
    w = r * countRope
    result.append(w)

print(max(result))
