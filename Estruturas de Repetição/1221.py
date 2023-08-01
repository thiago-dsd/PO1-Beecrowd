# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n = int(input())
for _ in range(n):
    i = int(input())
    if i <= 3:
        if i > 1:
            print('Prime')
        else:
            print('Not Prime')
    else:
        ultimo = int(i**0.5)
        if i % 2 == 0 or i % 3 == 0:
            print('Not Prime')
        else:
            for k in range(5, ultimo+1, 2):
                if i % k == 0:
                    print('Not Prime')
                    break
            else:
                print('Prime')

