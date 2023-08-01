# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

while (N := int(input())) != 0:
    seq = list(map(int, input().split()))
    picos = 0
    if N > 2:
        # checar o primeiro ponto
        # checa: e vale ou crista
        if (seq[0] < seq[-1] and seq[0] < seq[1]) \
        or (seq[0] > seq[-1] and seq[0] > seq[1]):
            picos += 1
        # Checar o ultimo ponto
        # checa: e vale ou crista
        if (seq[-1] < seq[-2] and seq[-1] < seq[0]) \
        or (seq[-1] > seq[-2] and seq[-1] > seq[0]):
            picos += 1
        # Checar até i=N-3, pois em i=N-1, N estará sendo checado e erro, mas N já foi 
        # checado, e em i=N-2, seq[i+2] = seq[N-2+2] = seq[N] -> erro!
        for i in range(N-2):
            # Trabalhar em trios para checar o do meio
            # checa: e vale ou crista
            if (seq[i+1] < seq[i] and seq[i+1] < seq[i+2]) \
            or (seq[i+1] > seq[i] and seq[i+1] > seq[i+2]):
                picos += 1
    else:
        # nao pode ter apenas 1 elemento
        # se tier 2 elementos, seq = [k, j] -> 1 crista e 1 vale -> 2 picos
        picos = 2
    print(picos)

