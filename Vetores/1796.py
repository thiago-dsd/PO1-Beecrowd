# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

q = int(input())
pessoas = map(int, input().split())
de_acordo = 0

for p in pessoas:
    if p == 0:
        de_acordo += 1

if de_acordo > q//2:
    print('Y')
else:
    print('N')

