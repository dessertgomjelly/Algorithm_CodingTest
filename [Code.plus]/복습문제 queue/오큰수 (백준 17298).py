from collections import deque
import sys

input = sys.stdin.readline

# 입력 받기
n = int(input())
a = list(map(int, input().split()))

# 결과값을 저장할 리스트, 초기값은 모두 -1로 설정
rs = [-1] * n

# 인덱스를 저장할 스택
stack = deque()

# 첫 번째 인덱스를 스택에 추가
stack.append(0)

# 두 번째 원소부터 순회 시작
for i in range(1, n):
    # 스택이 비어있지 않고, 현재 원소가 스택의 top에 해당하는 원소보다 클 경우
    while stack and a[stack[-1]] < a[i]:
        # 스택의 top에 해당하는 인덱스의 값을 현재 원소로 갱신
        rs[stack.pop()] = a[i]
    # 현재 인덱스를 스택에 추가
    stack.append(i)

# 결과 출력
print(*rs)
