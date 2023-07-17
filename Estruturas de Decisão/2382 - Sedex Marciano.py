l, a, p, r = input().split()
l = float(l)
a = float(a)
p = float(p)
r = float(r)
d = ((l)**2 + (p)**2)**(1/2)
D = ((d)**2 + (a)**2)**(1/2)
if D <= (r*2):
    print('S')
else:
    print('N')

