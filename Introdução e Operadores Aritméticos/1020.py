# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

tot_dias = int(input())

anos, resto = divmod(tot_dias, 365)
meses, resto = divmod(resto, 30)
dias = resto

print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')

