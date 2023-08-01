# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

comps = list(map(int, input().split()))
maior = max(comps)
comps.remove(maior)
print(max(comps))

