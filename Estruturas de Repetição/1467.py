# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

while True:
    try:
        a, b, c = input().split()
    except EOFError:
        break
    else:
        if a != b or a != c or b != c:
            if a == b or a == c:
                if b == a:
                    print('C')
                else:
                    print('B')
            else:
                print('A')
        else:
            print('*')
