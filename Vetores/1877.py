# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

# k picos alternados com k-1 vales

# Duas torre consecutivas nunca terão a mesma altura.

# primeira torre ate o primeiro pico: ordem crescente
# ultimo pico ate a ultima torre: ordem decrescente

# Vale existe em um intervalo [A, B] se B ≥ A+2 e 
# existe alguma torre J, A ≤ J ≤ B, tal que as alturas 
# das torres no intervalo [A,J] estão em ordem decrescente, 
# e as alturas das torres no intervalo [J,B] estão em ordem crescente.

# checar:
#    (1) existem k picos
#    (2) k picos alternados com k-1 vales
#    (3) As alturas das torres no intervalo [1, T1] estão em ordem crescente;
#    (4) Existe um "vale" no intervalo [Ti, Ti+1], para todo 1 ≤ i < K;
#    (5) As alturas das torres no intervalo [TK, N] estão em ordem decrescente.

n, k = map(int, input().split())
torres = list(map(int, input().split()))
ugly = False

# achar os picos e vales (ordenados por indice)
picos = []
vales = []
for i in range(1, len(torres)-1):
    if torres[i-1] < torres[i] and torres[i] > torres[i+1]:
        picos.append(i)
        
    elif torres[i-1] > torres[i] and torres[i] < torres[i+1]:
        vales.append(i)

# checar (1)
if k != len(picos):
    ugly = True

# checar (2)
if len(vales) != k - 1:
    ugly = True

if not ugly:
    # checar (3)
    for i in range(picos[0]):
        if torres[i] > torres[i+1]:
            ugly = True
            break

if not ugly:
    # checar (5)
    for i in range(picos[-1], len(torres)-1):
        if torres[i] < torres[i+1]:
            ugly = True
            break

if not ugly:
    # checar (4)
    for i in range(len(picos)-1):
        anterior = picos[i]
        proximo = picos[i+1]
        
        # pegar o vale atual
        for j in vales:
            if j > anterior and j < proximo:
                vale = j
                break
        
        for j in range(anterior, vale):  # precisa estar em ordem decrescente
            if torres[j] < torres[j+1]:
                ugly = True
                break
        
        for j in range(vale, proximo):  # precisa estar em ordem crescente
            if torres[j] > torres[j+1]:
                ugly = True
                break
    
if ugly:
    print('ugly')
else:
    print('beautiful')

