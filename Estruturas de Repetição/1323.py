# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

# 1x1: 1²
# 2x2: 2² + 1²
# 3x3: 3² + 2² + 1²
# 4x4: 4² + 3² + 2² + 1²
# nxn: n² + (n-1)² + (n-2)² + ... + 1²

while True:
    n = int(input())
    if n == 0:
        break
    else:
        c = 0
        for i in range(1, n+1):
            c += i**2
        print(c)

