# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

tot_secs = int(input())

horas, resto = divmod(tot_secs, 3600)
mins, resto = divmod(resto, 60)
secs = resto

print(f'{horas}:{mins}:{secs}')
    
