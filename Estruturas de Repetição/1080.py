# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

maior = int(input())
i_maior = 1
for i in range(2, 101):
    k = int(input())
    if k > maior:
        maior = k
        i_maior = i

print(maior)
print(i_maior)
