# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n, c = map(int, input().split())
p = 0
passou = False

for _ in range(n):
    s, e = map(int, input().split())
    p -= s
    p += e
    
    if p > c:
        passou = True

if passou:
    print('S')
else:
    print('N')
