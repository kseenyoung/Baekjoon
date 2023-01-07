import sys

n = int(sys.stdin.readline())
words = []

for _ in range(n):
    words.append(sys.stdin.readline().strip()) #strip() : white space 제거

set_words = set(words)
words = list(set_words)

words.sort()
words.sort(key=len)

for i in words:
    print(i)
