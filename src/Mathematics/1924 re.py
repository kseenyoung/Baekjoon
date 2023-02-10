from sys import stdin

input = stdin.readline

weeks = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = 0
M, D = map(int, input().split())

for i in range(M-1):
    day += month[i]
day += D
print(weeks[day % 7])
