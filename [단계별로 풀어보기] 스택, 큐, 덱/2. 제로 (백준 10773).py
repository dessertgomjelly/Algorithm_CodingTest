import sys

input = sys.stdin.readline

k = int(input())
st = []

for _ in range(k):
    x = int(input())
    if x > 0:
        st.append(x)
    elif x == 0:
        st.pop()

rs = 0
for num in st:
    rs += num

print(rs)