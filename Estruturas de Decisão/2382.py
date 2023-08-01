# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

inputs = map(int, input().split())
L_2, A_2, P_2, R_2 = map(lambda x: pow(x, 2), inputs)

if A_2 + P_2 <= 4 * R_2 and A_2 + L_2 <= 4 * R_2 and L_2 + P_2 <= 4 * R_2:
    print('S')
else:
    print('N')

