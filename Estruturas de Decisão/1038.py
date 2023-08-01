# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

item, qtd = map(int, input().split())

if item == 1:
    preco = 4
elif item == 2:
    preco = 4.5
elif item == 3:
    preco = 5
elif item == 4:
    preco = 2
else:
    preco = 1.5

print(f'Total: R$ {preco * qtd:.02f}')

