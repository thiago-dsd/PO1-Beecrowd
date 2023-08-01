# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

# diferenca: minuscula p/ maiuscula ou vice-versa
# precisa de 2 ou mais diferencas para ser falso:
# comparar elemento a elemento e verificar se sao iguais


while True:
    n = int(input())
    
    if n == 0:
        break
    
    else:
        # criacao do dicionario de assinaturas
        alunos = {}
        for _ in range(n):
            aluno, ass = input().split()
            alunos[aluno] = ass
    
        i = int(input())

        c = 0
        for _ in range(i):
            erradas = 0
            aluno, ass = input().split()
            
            for l in range(len(ass)):
                if alunos[aluno][l] != ass[l]:
                    erradas += 1
            
            if erradas >= 2:
                c += 1
        
        print(c)
