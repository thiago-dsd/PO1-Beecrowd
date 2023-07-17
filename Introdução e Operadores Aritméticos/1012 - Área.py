# -*- coding: utf-8 -*-

num = input()
A1, B1, C1 = num.split()
A = float(A1)
B = float(B1)
C = float(C1)
print('TRIANGULO: {:.3f}'.format(A*C/2))
print('CIRCULO: {:.3f}'.format(C*C*3.14159))
print('TRAPEZIO: {:.3f}'.format((A+B)/2*C))
print('QUADRADO: {:.3f}'.format(B*B))
print('RETANGULO: {:.3f}'.format(A*B))
