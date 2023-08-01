# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n1, n2, n3, n4 = map(float, input().split())

m = (n1*2 + n2*3 + n3*4 +n4*1)/10
print(f'Media: {m:.1f}')

if m >= 7:
    print('Aluno aprovado.')
elif m >= 5:
    print('Aluno em exame.')
    exame = float(input())
    print(f'Nota do exame: {exame:.1f}')
    final = (m + exame) / 2
    if final > 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {final:.1f}')
else:
    print('Aluno reprovado.')
