# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

while (entrada := input()) != '0 0 0':
    # P: col, N: lin
    P, N, C = map(int, entrada.split())
    matriz = []
    c = 0
    for _ in range(N):
        matriz.append(list(map(int, input().split())))
    for i in range(P):  # Checar as diferentes listas na posicao p
        tmp = 0
        for j in range(N):
            if matriz[j][i] == 1:  # inicia ou continua um palito
                tmp += 1
            else:  # se cortar ou nao comecar um palito, volta a zero o tam do palito
                if tmp >= C:
                    c += 1
                tmp = 0
        if tmp >= C:
            c += 1
    print(c)
