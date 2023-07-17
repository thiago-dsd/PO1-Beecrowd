a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
if a < b + c and b < a + c and c < a + b:
    if b == c and a == c and a == b:
        print('Valido-Equilatero')
    elif b != c and b != a and a != c:
        print('Valido-Escaleno')
    else:
         print('Valido-Isoceles')
    if ((a**2) == (b**2) + (c**2)) or ((b**2) == (a**2) + (c**2)) or ((c**2) == (b**2) + (a**2)):
        print('Retangulo: S')
    else:
        print('Retangulo: N')  
else:
    print('Invalido')

