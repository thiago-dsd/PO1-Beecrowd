# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

while (entrada := list(map(int, input().split()))) != [0, 0, 0, 0]:
    X1, Y1, X2, Y2 = entrada
    if X1 == X2 and Y1 == Y2:  # mesmas posicoes
        print(0)
    elif X1 == X2 or Y1 == Y2:  # mesma linha ou coluna
        print(1)
    else:
        for i in range(1, X1):
            if X2 == X1-i and (Y2 == Y1-i or Y2 == Y1+i):  # diagonais à esquerda
                print(1)
                break
        else:
            for i in range(1, 9-X1):  # (8 - X1) + 1 = 9 - X1
                if X2 == X1+i and (Y2 == Y1-i or Y2 == Y1+i):  # diagonais à direita
                    print(1)
                    break
            else:  # qualquer outra posição
                print(2)

