# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

valido = True
for i in range(5):
    if l1[i] == l2[i]:
        valido = False
        break

if valido:
    print('Y')
else:
    print('N')
