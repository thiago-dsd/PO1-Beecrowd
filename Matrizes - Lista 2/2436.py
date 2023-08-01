# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

cima = lambda a, b, m: m[a-1][b] == 1
baix = lambda a, b, m: m[a+1][b] == 1
esqu = lambda a, b, m: m[a][b-1] == 1
dire = lambda a, b, m: m[a][b+1] == 1

def verifica(a, b, l, c, m, a_ant=-1, b_ant=-1):
    if l == 1 or c == 1:
        if l == 1 and c == 1:  # apenas um quadrado
            return a, b
        elif l == 1: # apenas 1 linha, verificar apenas esqu e dire
            if b == 0:
                if dire(a, b, m) and b+1 != b_ant:
                    return a, b+1
                else:
                    return a, b
            elif b == c-1:
                if esqu(a, b, m) and b-1 != b_ant:
                    return a, b-1
                else:
                    return a, b
            else:
                if dire(a, b, m) and b+1 != b_ant:
                    return a, b+1
                elif esqu(a, b, m) and b-1 != b_ant:
                    return a, b-1
                else:
                    return a, b
        else:  # apenas 1 coluna, verificar apenas cima e baix
            if a == 0:
                if baix(a, b, m) and a+1 != a_ant:
                    return a+1, b
                else:
                    return a, b
            elif a == l-1:
                if cima(a, b, m) and a-1 != a_ant:
                    return a-1, b
                else:
                    return a, b
            else:
                if cima(a, b, m) and a-1 != a_ant:
                    return a-1, b
                if baix(a, b, m) and a+1 != a_ant:
                    return a+1, b
                else:
                    return a, b
            
    else:
        if a == 0:
            if baix(a, b, m) and a+1 != a_ant:
                return a+1, b
            else:
                if b == 0:
                    if dire(a, b, m) and b+1 != b_ant:
                        return a, b+1
                    else:
                        return a, b
                elif b == c-1:
                    if esqu(a, b, m) and b-1 != b_ant:
                        return a, b-1
                    else:
                        return a, b
                else:
                    if dire(a, b, m) and b+1 != b_ant:
                        return a, b+1
                    elif esqu(a, b, m) and b-1 != b_ant:
                        return a, b-1
                    else:
                        return a, b
                    
        elif a == l-1:
            if cima(a, b, m) and a-1 != a_ant:
                return a-1, b
            else:
                if b == 0:
                    if dire(a, b, m) and b+1 != b_ant:
                        return a, b+1
                    else:
                        return a, b
                elif b == c-1:
                    if esqu(a, b, m) and b-1 != b_ant:
                        return a, b-1
                    else:
                        return a, b
                else:
                    if dire(a, b, m) and b+1 != b_ant:
                        return a, b+1
                    elif esqu(a, b, m) and b-1 != b_ant:
                        return a, b-1
                    else:
                        return a, b

        elif b == 0:
            if cima(a, b, m) and a-1 != a_ant:
                return a-1, b
            if baix(a, b, m) and a+1 != a_ant:
                return a+1, b
            if dire(a, b, m) and b+1 != b_ant:
                return a, b+1
            else:
                return a, b 
            
        elif b == c-1:
            if cima(a, b, m) and a-1 != a_ant:
                return a-1, b
            if baix(a, b, m) and a+1 != a_ant:
                return a+1, b
            if esqu(a, b, m) and b-1 != b_ant:
                return a, b-1
            else:
                return a, b

        else:
            if cima(a, b, m) and a-1 != a_ant:
                return a-1, b
            if baix(a, b, m) and a+1 != a_ant:
                return a+1, b
            if esqu(a, b, m) and b-1 != b_ant:
                return a, b-1
            if dire(a, b, m) and b+1 != b_ant:
                return a, b+1
            else:
                return a, b
        
L, C = map(int, input().split())
A, B = map(int, input().split())
A, B = A-1, B-1
m = []

for i in range(L):
    tmp = list(map(int, input().split()))
    m.append(tmp)

a_ant, b_ant = A, B  # primeira posicao
a, b = verifica(A, B, L, C, m) # segunda posicao
while True:
    # n_a: proximo a, a: a atual, a_ant: a anterior 
    n_a, n_b = verifica(a, b, L, C, m, a_ant, b_ant)
    if n_a == a and n_b == b:
        print(n_a+1, n_b+1)  # ir de index para posição real
        break
    a_ant, b_ant = a, b
    a, b = n_a, n_b

