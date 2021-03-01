a = int(input())
b = int(input())
max_passwords_count = int(input())

s1 = 35
s2 = 64

for d3 in range(1, a + 1):
    for d4 in range(1, b + 1):
        print(f"{chr(s1)}{chr(s2)}{d3}{d4}{chr(s2)}{chr(s1)}", end="|")
        s1 += 1
        if s1 > 55:
            s1 = 35
        s2 += 1
        if s2 > 96:
            s2 = 64
        max_passwords_count -= 1
        if max_passwords_count == 0:
            exit()
