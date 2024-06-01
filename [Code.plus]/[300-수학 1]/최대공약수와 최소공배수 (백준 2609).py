"""
6 | 24 18
  |  4  3

최대 공약수 ? 둘다 나눠지는 가장 큰 수
최소 공배수 둘다 나눠지는 가장 큰수에 나머지를 곱한것.

"""

a = list(map(int,input().split()))
a.sort()
x, y = a[0], a[1]

#최대 공약수를 구하는 함수(유클리드 호제법)
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y / gcd(x,y)


print(gcd(x,y))
print(int(lcm(x,y)))