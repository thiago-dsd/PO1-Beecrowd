# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

# nao e certeza de que e triang. ret.
# calcular com det

n = int(input())
for _ in range(n):
    x1, y1, x2, y2, x3, y3 = map(float, input().split())
    
    det = (x1*y2 + x3*y1 + x2*y3) - (x2*y1 + x1*y3 + x3*y2)
    area = 0.5 * abs(det)
    
    print(f'{area:.3f}')
