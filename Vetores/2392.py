# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

p, s = map(int, input().split())

pedras = [0] * p

for _ in range(s):
    atual, passo = map(int, input().split())
    for i in range(atual-1, p, passo):
        pedras[i] = 1
    for i in range(atual-1, -1, -passo):
        pedras[i] = 1

for i in pedras:
    print(i)
