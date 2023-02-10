string = input()

answer = []

for s in string:
    num = ord(s)
    if s.isupper():
        if s > 'M':
            answer.append(chr(num - 13))
        else:
            answer.append(chr(num + 13))
    elif s.islower():
        if s > 'm':
            answer.append(chr(num - 13))
        else:
            answer.append(chr(num + 13))
    else:
        answer.append(s)

print(''.join(answer))