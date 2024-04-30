import sys

input = sys.stdin.readline

while True:
    S = input().strip()
    stack = []
    if S == '.':
        print('yes')
        break
    result = True
    for chk in S:
        if chk == '(' or chk == '[':
            stack.append(chk)
        elif chk == ')':
            if not stack or stack[-1] != '(':
                result = False
                break
            stack.pop()
        elif chk == ']':
            if not stack or stack[-1] != '[':
                result = False
                break
            stack.pop()

    print('yes' if result and not stack else 'no')
