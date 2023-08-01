# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
i = int(input())
cont = 0
for _ in range(i):
    l, c = map(int, input().split())
    if l > c:
        cont += c
print(cont)
