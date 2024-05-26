s = input()

alpha = 'abcdefghijklmnopqrstuvwxyz'
rs = [-1]*26

for index, char in enumerate(s):
    pos = alpha.index(char)
    if rs[pos] == -1:
        rs[pos] = index

print(*rs)