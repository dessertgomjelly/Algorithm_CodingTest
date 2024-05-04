a, b = map(int, input().split())

def gcd(a,b):
    while b:
        temp = b
        b = a % b
        a = temp
    return a

print(a*b//gcd(a,b))