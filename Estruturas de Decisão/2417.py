# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

c1, c2, c3, f1, f2, f3 = map(int, input().split())

pc = c1 * 3 + c2 * 1
pf = f1 * 3 + f2 * 1

if pc > pf:
    print('C')
elif pf > pc:
    print('F')
else:
    if c3 > f3:
        print('C')
    elif f3 > c3:
        print('F')
    else:
        print('=')

