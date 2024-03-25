"""
10진법에서 B진법으로 변하는방법

10진수 에서 2진수로 하려면

10/2

remainder = 10 % 2
5

나눌수있을떄까지 나눈 다음에? 더하기 나머지.

나눌수있을때까지란 remainder 가 해당진수보다 클때.


2|10...
2|5 ...0
2|2...1
 1...0


뒤에서부터 읽어. 1010 한다음에 아까한대로 진수 곱하면돼.
"""
N, B = map(int, input().split())

# B진법으로 변환 시 사용하는 알파벳 문자열입니다.
alphabet_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# 10진수를 B진법으로 변환하는 함수입니다.
def convert_to_base(N, B):
    if N == 0:  # 예외 처리: 만약 N이 0이라면, '0'을 반환합니다.
        return '0'

    result = ''
    while N > 0:
        remainder = N % B
        result = alphabet_list[remainder] + result  # 나머지를 결과 문자열의 앞에 추가합니다.
        N //= B

    return result

# 10진수 N을 B진법으로 변환합니다.
result = convert_to_base(N, B)

# 결과를 출력합니다.
print(result)
