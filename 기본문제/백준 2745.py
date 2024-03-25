"""
B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램.

1,2,3,4,5,6,7,8,9,10,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z

1100 (2)

0 x 2^0 +


"""
import sys

input = sys.stdin.readline

alphabet_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'



N, B = input().split()
B = int(B)
num = []

for char in N:
    for i, alphabet in enumerate(alphabet_list):
        if char == alphabet:
            num.append(i)

# num[::-1]부터 * B^0 + B^1
result = 0
for i, number in enumerate(num[::-1]):
    result += number * (B ** i)

print(result)

