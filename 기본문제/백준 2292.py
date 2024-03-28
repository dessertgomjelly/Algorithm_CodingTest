"""
i = 1
1 : 1 (1개)
2 : 234567 (6개)  i + 1
3 : 8 9 10 11 12 13 14 15 16 17 18 19 (12개) 2i


"""

import sys

input = sys.stdin.readline

N = int(input())

def find_floor(room_number):
    if room_number == 1:
        return 1
    else:
        count = 1
        total_room = 1                  #최종적으로 토탈룸보다 작아야하니깐.
        while room_number > total_room: #마지막 방보다 클때까지 계속 돌려.
            total_room = total_room + 6 * count
            count += 1
        return count

print(find_floor(N))