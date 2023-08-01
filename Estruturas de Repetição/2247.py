# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
c = 0
while (N := int(input())) != 0:
    c += 1
    tmp = 0
    print('Teste', c)
    for i in range(N):
        J, Z = map(int, input().split())
        tmp += J - Z
        print(tmp)
    print()

