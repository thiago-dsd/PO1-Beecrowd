# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
i = 1
while True:
    v = int(input())
    if v == 0:
        break
    else:
        c_50, r = divmod(v, 50)
        c_10, r = divmod(r, 10)
        c_5, r = divmod(r, 5)
        c_1 = r
        
        print('Teste', i)
        print(c_50, c_10, c_5, c_1)
        
        print()
        i += 1
