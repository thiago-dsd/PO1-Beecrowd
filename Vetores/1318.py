# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    else:
        T = list(map(int, input().split()))
        c = 0
        for i in list(set(T)):
            if T.count(i) > 1:
                c += 1
        print(c)
