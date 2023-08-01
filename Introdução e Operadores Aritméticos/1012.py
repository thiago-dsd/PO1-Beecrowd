# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

PI = 3.14159

A, B, C = map(float, input().split())

a_tria = (A * C) / 2
a_circ = PI * C * C
a_trap = ((A + B) * C) / 2
a_quad = B * B
a_reta = A * B

print(f'TRIANGULO: {a_tria:.3f}')
print(f'CIRCULO: {a_circ:.3f}')
print(f'TRAPEZIO: {a_trap:.3f}')
print(f'QUADRADO: {a_quad:.3f}')
print(f'RETANGULO: {a_reta:.3f}')

