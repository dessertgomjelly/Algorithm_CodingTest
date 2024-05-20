from collections import deque

data = input()

stack = deque()
ans = ''
check = False # 괄호안의 여부를 체크
for d in data:
    # 스택에 존재하는 값을 역으로 추가
    if d == '<':
        check = True
        while stack:
            ans += stack.pop()

    stack.append(d)
    # 스택에 존재하는 값은 괄호안의 값이기에 순차적으로 추가
    if d == '>':
        check = False
        while stack:
            ans += stack.popleft()
    # 스택에 존재하는 값을 역으로 추가
    if d == ' ' and not check:
        for i in range(len(stack)):
            if i == 0:
                stack.pop()
                continue
            ans += stack.pop()
        ans += ' '  # 공백 추가

# 스택에 값이 남아있는 경우는 괄호의 경우가 아니기에 역으로 추가
while stack:
    ans += stack.pop()

print(ans)
