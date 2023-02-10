from sys import stdin

for line in stdin:
    try:
        print(line, end="")
    except EOFError:
        break