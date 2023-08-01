# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n = int(input())
for _ in range(n):
    tmp = int(input())
    if tmp == 0:
        print('NULL')
    elif tmp % 2 == 0:
        print('EVEN', end=' ')
    else:
        print('ODD', end=' ')
    if tmp < 0:
        print('NEGATIVE')
    elif tmp > 0:
        print('POSITIVE')
