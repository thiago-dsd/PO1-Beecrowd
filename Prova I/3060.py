# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

v = int(input())
p = int(input())

r = v % p

for _ in range(p):
    p_atual = v // p
    if r > 0:
        p_atual += 1
        r -= 1
    print(p_atual)
