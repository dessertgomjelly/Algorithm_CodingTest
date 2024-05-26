s = input()
rs = []

for char in s:
    if char.isalpha():
        rs.append(chr((ord(char)+13%26)))
    else:
        rs.append(char)

print(* rs)
