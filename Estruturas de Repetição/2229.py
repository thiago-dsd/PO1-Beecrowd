# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

c = 1
while True:
    i = int(input())
    if i == -1:
        break
    else:
        print(f'Teste {c}')
        # relação encontrada ao realizar os testes
        k = (1 + 2**i)**2
        print(k)
        print()
        c += 1 

