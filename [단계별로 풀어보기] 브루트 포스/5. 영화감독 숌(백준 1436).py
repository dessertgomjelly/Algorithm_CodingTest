"""
종말의 수는 어떤 수에 적어도6이 3개 이상 연속으로 들어가는 수
N번째 영화.

숫자를 하나씩 올린다음에, 666이 들어가면 cnt +1 cnt+3 이면 종말의수.

종말의 수를 리스트에 넣고, n번째 반환.
"""

N = int(input())

result = []
num = 0

while True:
    num += 1
    str_num = str(num)
    if "666" in str_num:  # 변환된 문자열에서 "666"이 포함되어 있는지 확인
        result.append(num)
        if len(result) == N:
            break

print(result[-1])
