import sys

input = sys.stdin.readline

p = []

for _ in range(3):
    N = int(input())
    p.append(N)

# Check if sum of angles is 180
if sum(p) == 180:
    if len(set(p)) == 1:  # All angles are equal
        print("Equilateral")
    elif len(set(p)) == 2:  # Two angles are equal
        print("Isosceles")
    else:  # No angles are equal
        print("Scalene")
else:
    print("Error")
