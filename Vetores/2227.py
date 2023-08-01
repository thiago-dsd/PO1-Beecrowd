# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

c = 0
while True:
    A, V = map(int, input().split())
    if A == 0 and V == 0:
        break
    else:
        c += 1
        aero = {str(x): 0 for x in range(1, A+1)}
        for i in range(V):
            partida, chegada = input().split()
            aero[partida] += 1
            aero[chegada] += 1
        maior = max(aero.values())
        maiores = []
        # k já está em ordem por conta da construcao usando range
        for k, v in aero.items():
            if v == maior:
                maiores.append(k)
        # erro de apresentacao onde?
        print('Teste', c)
        print(' '.join(maiores) + ' ')
        print('')
