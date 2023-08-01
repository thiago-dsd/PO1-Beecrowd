n, g = [int(x) for x in input().split()]

runas = {}
for _ in range(n):
    r, v = input().split()
    runas[r] = int(v)

input()
rec = input().split()

tot = 0
for runa in rec:
    tot += runas[runa]

print(tot)
if tot >= g:
    print('You shall pass!')
else:
    print('My precioooous')
