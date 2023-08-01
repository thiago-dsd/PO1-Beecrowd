# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

a, b, c = map(float, input().split())

if abs(a-b) < c and c < a+b \
    and abs(a-c) < b and b < a+c \
    and abs(b-c) < a and a < b+c:
        print('Perimetro =', a+b+c)
else:
    print(f'Area = {(a+b)*c/2:.1f}')

