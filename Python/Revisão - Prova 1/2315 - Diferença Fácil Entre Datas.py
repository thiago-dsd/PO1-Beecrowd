m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
d1, m1 = input().split()
d2, m2 = input().split()
d1 = int(d1)
m1 = int(m1)
d2 = int(d2)
m2 = int(m2)
total = 0
if m1 != m2:
    total += m[m1 - 1] - d1
    for c in range (m1 +1, m2):
        total += m[c - 1]
    total += d2
else:
    total = d2 - d1
print(total)


