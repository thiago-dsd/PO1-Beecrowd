# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

# Razões: 2 f, 3 o e 5 l
# preciso descobrir o mdc de f, o, l
# pego o menor valor entre eles -> não pode existir divisor k de um 
# número n tq k > n
# itero de 1 até o menor valor checando os divisores
# paro quando chegar no menor valor entre eles
# APLICAR RAZÕES!

f, o, l = map(int, input().split())

min_valor = min([f, o, l])

mdc = 0
for i in range(1, min_valor+1):
    if f >= i*2 and o >= i*3 and l >= i*5:
        mdc = i

print(mdc)
