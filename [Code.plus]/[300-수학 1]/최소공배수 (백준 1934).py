n = int(input())


#최대 공약수를 구하는 함수(유클리드 호제법)
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y / gcd(x,y)


for _ in range(n):
    a = list(map(int,input().split()))
    a.sort()
    x, y = a[0], a[1]
    print(int(lcm(x, y)))


