#TRIÂNGULO
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
if a < b + c and b < a + c and c < b + a:
    print('Perimetro = {:.1f}'.format(a + b + c))
else:
    print('Area = {:.1f}'.format(((a+b)/2)*c))
    

