# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

SENHA = 2002

while True:
    if (tentativa := int(input())) == SENHA:
        print('Acesso Permitido')
        break
    else:
        print('Senha Invalida')

