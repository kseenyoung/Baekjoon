word = input()
nword = ''

for i in range(len(word)):
    if word[i].isupper(): #대문자일 때
        nword += word[i].lower()
    else:
        nword += word[i].upper()

print(nword)