# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

# aqueles com média menor ou igual a 127 serão considerados pretos e 
# aqueles com média maior a 127 serão considerados brancos.

itens = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}

while True:
    n = int(input())
    
    if n == 0:
        break
    else:
        for _ in range(n):
            tmp = map(int, input().split())
            brancos = []
            pretos = []
            
            for k, v in enumerate(tmp):
                if v <= 127:
                    pretos.append(k)
                else:
                    brancos.append(k)
                    
            if len(pretos) != 1:
                print('*')
            else:
                print(itens[pretos[0]])
        

