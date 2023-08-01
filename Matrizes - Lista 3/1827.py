# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

# (a) diag princ (2): i == j
# (b) diag secun (3): j + i == tam-1
# (c) quad com '1': quadrado que comeca em tam//3 ->i,j no intervalo [tam//3, len(m)-tam//3]
# (d) meio da matriz: quando i == j == (len(matriz)-1)//2
# precedencia (menor -> maior): (a), (b), (c), (d)
# deixar os com maior precedencia antes -> checados primeiro e pula o resto


while True:
    try:
        tam = int(input())
    except EOFError:
        break
    else:
        m = []
        c = 0  # p/ diag sec
        range_meio = list(range((tam//3), tam-tam//3))
        for i in range(tam):
            tmp = []
            for j in range(tam):
                if i == j and i == (tam-1)//2:
                    tmp.append(4)

                elif i in range_meio and j in range_meio:
                    tmp.append(1)

                elif i == j:
                    tmp.append(2)

                elif j + i == tam-1:
                    tmp.append(3)
                
                else:
                    tmp.append(0)
            c += 1
            m.append(tmp)

        for i in range(tam):
            for j in range(tam):
                print(m[i][j], end='')
            print()
        
        print()
