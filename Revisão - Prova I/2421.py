# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

# soma das alturas, e apenas maior largura

px, py = map(int, input().split())
f1x, f1y = map(int, input().split())
f2x, f2y = map(int, input().split())

if max([f1x, f2x]) <= px and f1y + f2y <= py:
    print('S')
elif max([f1y, f2x]) <= px and f1x + f2y <= py:
    print('S')
elif max([f1x, f2y]) <= px and f1y + f2x <= py:
    print('S')
elif max([f1y, f2y]) <= px and f1x + f2x <= py:
    print('S')
elif max([f1x, f2x]) <= py and f1y + f2y <= px:
    print('S')
elif max([f1y, f2x]) <= py and f1x + f2y <= px:
    print('S')
elif max([f1x, f2y]) <= py and f1y + f2x <= px:
    print('S')
elif max([f1y, f2y]) <= py and f1x + f2x <= px:
    print('S')
else:
    print('N')

