# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

c = int(input())
for _ in range(c):
    n = int(input())
    
    xb, yb = map(int, input().split())
    x, y = map(int, input().split())
    
    i_menor = 1
    menor_dist = ((xb-x)**2 + (yb - y)**2)**0.5
    
    for i in range(2, n+1): # 0 ~ n-1 = 2 ~ n+1
        x, y = map(int, input().split())
        dist = ((xb-x)**2 + (yb - y)**2)**0.5
        
        if dist < menor_dist:
            menor_dist = dist
            i_menor = i
            
    print(i_menor)
