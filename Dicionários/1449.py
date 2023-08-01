# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n = int(input())
for _ in range(n):
    n_palavras, n_linhas = map(int, input().split())
    
    # criacao do dicionario com as traducoes
    palavras = {}
    for _ in range(n_palavras):
        jap = input()
        por = input()
        palavras[jap] = por
    
    for _ in range(n_linhas):
        # apenas 1 palavra em japones por vez
        trad = []
        linha = input().split()
        for p in linha:
            if p in palavras:
                trad.append(palavras[p])
            else:
                trad.append(p)
        
        print(' '.join(trad))
    
    print()
