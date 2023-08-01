# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

# se alguem passa em 1 e outro em 4, comecara em 1 e terminara em 14: 14 total
# 1º em 5 e 2º em 6: comecara em 5 e terminara em 6+10 = 11 total
# está dando maior

n = int(input())

lista = []
for _ in range(n):
    lista.append(int(input()))

lista.sort()

t = 10

for i in range(1, len(lista)):
    if lista[i] - lista[i-1] < 10:
        t += lista[i] - lista[i-1]
    else:
        t += 10

print(t)
