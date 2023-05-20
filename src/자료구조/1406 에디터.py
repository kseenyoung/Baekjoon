import sys
input = sys.stdin.readline

string = list(input().rstrip()) #rstrip : 화이트스페이스 제거
n = int(input())
position = len(string)

for _ in range(n):
    query = list(input().split())
    if query[0] == 'D':
        if position != len(string):
            position += 1
    elif query[0] == 'L':
        if position != 0:
            position -= 1
    elif query[0] == 'B':
        if position != 0:
            string.remove(string[position-1])
            position -= 1
    elif query[0] == 'P':
        string.insert(position, query[1])
        position += 1

print(''.join(string))