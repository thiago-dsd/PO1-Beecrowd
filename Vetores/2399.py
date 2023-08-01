# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

N = int(input())
nums = []
for k in range(N):  # range(0, N) -> se houver apenas 1 elemento
    nums.append(int(input()))  # acrescenta n ao final
    # checa apenas os 2 primeiros para verificar o primeiro
    # ou verifica apenas o 1º, caso tenha apenas 1 n
    if k == 1 or N == 1:  
        print(nums.count(1))
    if k >= 2:  # a partir do 2º n, verifica n por trios [n-1, n, n+1]
        print(nums.count(1))
        nums.pop(0)  # remove o 1º elemento     
        if k == N-1:
            print(nums.count(1)) # checa apenas os 2 ultimos para verificar o ultimo
