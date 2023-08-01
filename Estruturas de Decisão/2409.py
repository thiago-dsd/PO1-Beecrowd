# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

# Pegar as duas menores dimensões do colchão e comparar com as da porta

dim_colchao = list(map(int, input().split()))
dim_porta = list(map(int, input().split()))

c_min1 = min(dim_colchao)
dim_colchao.remove(c_min1)
c_min2 = min(dim_colchao)

p_min1 = min(dim_porta)
dim_porta.remove(p_min1)
p_min2 = dim_porta[0]

if c_min1 <= p_min1 and c_min2 <= p_min2:
    print('S')
else:
    print('N')
