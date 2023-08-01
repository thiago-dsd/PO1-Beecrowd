# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

list_l = list(map(int, input().split()))

if (abs(list_l[0] - list_l[1]) >= list_l[2] or list_l[2] >= list_l[0] + list_l[1]) or \
   (abs(list_l[0] - list_l[2]) >= list_l[1] or list_l[1] >= list_l[0] + list_l[2]) or \
   (abs(list_l[1] - list_l[2]) >= list_l[0] or list_l[0] >= list_l[1] + list_l[2]):
        print('Invalido')
else:
    print('Valido', end='-')
    
    qtd_iguais = len(set(list_l))
    if qtd_iguais == 1:
        print('Equilatero')
    elif qtd_iguais == 2:
        print('Isoceles')
    else:
        print('Escaleno')

    for l in list_l:
        tmp = list_l[:]
        tmp.remove(l)
        if l*l == sum(map(lambda x: pow(x, 2), tmp)):
            print('Retangulo: S')
            break
    else:
        print('Retangulo: N')
