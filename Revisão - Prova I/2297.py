# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

c = 1
while True:
    n = int(input())
    if n == 0:
        break
    else:
        n_a = n_b = 0
        for _ in range(n):
            a, b = map(int, input().split())
            n_a += a
            n_b += b
            
        print('Teste', c)
        if n_a > n_b:
            print('Aldo')
        else:
            print('Beto')
    
    print()
    c += 1
