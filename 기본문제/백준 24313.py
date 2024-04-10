"""
f(n) <= c * g(n)
"""

a1, a0 = map(int,input().split())
c = int(input())
n = int(input())

fn = a1 * n + a0
if fn <= c*n and a1<=c:
    print(1)
else:
    print(0)