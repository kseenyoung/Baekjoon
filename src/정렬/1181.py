import sys

input = sys.stdin.readline

N = int(input())
words = []
for i in range(N):
    word = input().strip()  # strip : 공백/개행 제거
    if word not in words:
        words.append(word)

words.sort(key=lambda x: (len(x), x))

for w in words:
    print(w)
