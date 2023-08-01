# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

d_1, m_1 = map(int, input().split())
d_2, m_2 = map(int, input().split())

s_1 = s_2 = 0

s_1 += sum(meses[:m_1-1])
s_1 += d_1

s_2 += sum(meses[:m_2-1])
s_2 += d_2

print(s_2 - s_1)

