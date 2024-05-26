import sys
input = sys.stdin.readline

while True:
    rs = input().strip()
    if not rs:
        break

    lowercase_count = 0
    uppercase_count = 0
    digit_count = 0
    space_count = 0

    for char in rs:
        if char.isalpha():
            if char.islower():
                lowercase_count += 1
            elif char.isupper():
                uppercase_count += 1
        elif char.isspace():
            space_count += 1
        elif char.isdigit():
            digit_count += 1
    print(lowercase_count, uppercase_count, digit_count, space_count)
