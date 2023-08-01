# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

# 1 de 4 -> 4 de 2 -> 16 de 1
# 1 de 9 -> 4 de 4.5 -> 16 de 2.25 -> 64 de x<2

n = int(input())
k = 1
while n >= 2:
    n /= 2
    k *= 4
print(k)
