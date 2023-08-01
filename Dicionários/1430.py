# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

# talvez problema com ponto flutuante

notas = {
    'W': 1,
    'H': 1/2,
    'Q': 1/4,
    'E': 1/8,
    'S': 1/16,
    'T': 1/32,
    'X': 1/64
    }

while True:
    entrada = input()
    if entrada == '*':
        break
    else:
        # equivalente a entrada[1:-2], porém mais explícito
        entrada = entrada.removeprefix('/')
        entrada = entrada.removesuffix('/')
        
        corretos = 0
        compassos = list(entrada.split('/'))
        for c in compassos:
            cont = 0
            for n in c:
                cont += notas[n]
            if cont == 1:
                corretos += 1
                
        print(corretos)
