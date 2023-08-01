# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n = int(input())
for _ in range(n):
    tmp = 0
    x, y = map(int, input().split())
    if x > y:
        for i in range(y+1, x):
            if i % 2 == 1:
                tmp += i
    elif x < y:
        for i in range(x+1, y):
            if i % 2 == 1:
                tmp += i
    print(tmp)
