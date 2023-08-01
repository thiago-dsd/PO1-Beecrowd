tot, min_p = [int(x) for x in input().split()]

p = [int(x) for x in input().split()]

a_tempo = 0
for i in p:
    if i <= 0:
        a_tempo += 1

if a_tempo >= min_p:
    print('YES')
else:
    print('NO')
