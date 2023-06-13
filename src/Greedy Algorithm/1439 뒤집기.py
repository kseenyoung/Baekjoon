S = input()

cnt = [0, 0]
flag = S[0]
cnt[int(flag)] += 1

for s in S:
    if flag != s:
        if s == '1':
            cnt[1] += 1
        if s == '0':
            cnt[0] += 1
        flag = s

print(min(cnt))