s = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'
rs = [0] * 26
for ss in s:
    rs[alpha.index(ss)] += 1

print(*rs)