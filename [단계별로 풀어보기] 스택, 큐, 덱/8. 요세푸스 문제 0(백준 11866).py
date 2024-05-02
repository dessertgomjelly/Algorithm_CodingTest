from collections import deque
n, k = map(int, input().split())

people = deque()
rs = []

for i in range(1,n+1):
    people.append(i)


while people:
    for _ in range(k-1):
        people.append(people.popleft())
    rs.append(people.popleft())


print("<", end="")
for i in rs:
    print(i, end="")
    if i != rs[-1]:
        print(end=", ")
print(">")