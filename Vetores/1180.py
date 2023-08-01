# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n = int(input())

val = map(int, input().split())
menor = next(val)
i_menor = 0

for i, v in zip(range(1, n), val):
    if v < menor:
        menor = v
        i_menor = i

print('Menor valor:', menor)
print('Posicao:', i_menor)
