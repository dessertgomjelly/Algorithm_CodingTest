s = input().strip()
rs = []

for char in s:
    if 'a' <= char <= 'z':  # 소문자
        rs.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
    elif 'A' <= char <= 'Z':  # 대문자
        rs.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
    else:  # 알파벳이 아닌 문자
        rs.append(char)

print("".join(rs))
