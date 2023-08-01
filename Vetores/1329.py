# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

# forma alternativa: usar val.count()!

while True:
    n = int(input())
    if n == 0:
        break
    else:
        val = map(int, input().split())
        m = j = 0
        for v in val:
            if v == 0:
                m += 1
            else:
                j += 1
        
        print(f'Mary won {m} times and John won {j} times')
