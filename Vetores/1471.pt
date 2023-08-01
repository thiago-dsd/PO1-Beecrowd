# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

while True:
    try:
        N, R = map(int, input().split())
    except EOFError:
        break
    else:
        if N == R:
            input()
            print('*')
        else:
            retornaram = set(map(int, input().split()))
            mergulharam = set(range(1, N+1))
            nao_retornaram = sorted(list(mergulharam - retornaram))
            print(' '.join([str(x) for x in nao_retornaram]) + ' ')

