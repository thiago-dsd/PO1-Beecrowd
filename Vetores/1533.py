# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

# forma alternativa: ordenar a lista e pegar lista[-2]!

while True:
    n = int(input())
    if n == 0:
        break
    else:
        tmp = map(int, input().split())
        maior = next(tmp)  # consome o 1 elemento do iterator e pega seu valor
        i_maior = i_seg_maior = v_seg_maior = 0  # v sempre sera > 0
        
        for k, v in zip(range(1, n), tmp):
            if v < maior and v > v_seg_maior:
                v_seg_maior = v
                i_seg_maior = k
            elif v > maior:
                v_seg_maior = maior
                i_seg_maior = i_maior
                maior = v
                i_maior = k
        
        print(i_seg_maior + 1)
