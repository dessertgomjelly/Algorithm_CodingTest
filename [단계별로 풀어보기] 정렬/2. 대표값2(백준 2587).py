num = []

for _ in range(5):
    n = int(input())
    num.append(n)

num.sort()

print(sum(num)//5)
print(num[2])