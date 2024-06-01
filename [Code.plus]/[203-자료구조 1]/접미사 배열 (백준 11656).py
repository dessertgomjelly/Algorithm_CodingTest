"""
1. 알파벳 순.?
"""

s = input().strip()
rs = []

for i in range(len(s)):
    rs.append(s[i:])

rs.sort()


for s in rs:
    print(s)

