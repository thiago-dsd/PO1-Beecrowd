# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

while True:
    try:
        h, m = map(int, input().split())
    except EOFError:
        break
    else:
        h_r = h//30
        m_r = m//6
        print(f'{h_r:02}:{m_r:02}')

