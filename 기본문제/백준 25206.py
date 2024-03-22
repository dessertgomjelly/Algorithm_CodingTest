"""
아이디어
- 입력 받기 : 리스트로 입력받기
- 학점 비교
"""

import sys

input = sys.stdin.readline

a=[4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0.0]
b=['A+','A0','B+','B0','C+','C0','D+','D0','F']

p = [0]*20

for i in range(20):
    p[i] = (input().split())

scores= []
grades = []
gg = []
total = 0

for i in p:
    if i[2] != 'P':
        score = float(i[1])
        grade = i[2]
        scores.append(score)
        grades.append(grade)
        index = b.index(grade)
        gg.append(a[index])

for i in range(len(gg)):
    total += gg[i] * scores[i]

print(total/sum(scores))
