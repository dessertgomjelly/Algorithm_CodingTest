import sys

input = sys.stdin.readline

N = int(input())

cards = list(map(int, input().split()))

M = int(input())

chk = list(map(int,input().split()))


card_dict = {}
for card in cards:
    card_dict[card] = True

for num in chk:
    if num in card_dict:
        print(1,end = ' ')
    else:
        print(0,end = ' ')
