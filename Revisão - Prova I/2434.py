# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n, s = map(int, input().split())
menor = s

for _ in range(n):
    m = int(input())
    s += m  # atualiza o saldo
    if s < menor:
        menor = s

print(menor)
