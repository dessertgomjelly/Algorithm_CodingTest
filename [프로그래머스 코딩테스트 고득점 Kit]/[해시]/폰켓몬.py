def solution(nums):
    choice = len(nums) // 2  # 초이스 횟수
    answer = 0
    chk = []

    for a in nums:
        if a not in chk:
            chk.append(a)
            answer += 1

    if answer > choice:
        return choice
    else:
        return answer

nums = list(map(int, input().split()))
print(solution(nums))
