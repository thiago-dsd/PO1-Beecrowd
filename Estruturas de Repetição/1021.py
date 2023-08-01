# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

# Problema do ponto flutuante!
k = float(input()) * 100

notas = {}
moedas = {}
notas['100.00'], resto = divmod(k, 10000)
notas['50.00'], resto = divmod(resto, 5000)
notas['20.00'], resto = divmod(resto, 2000)
notas['10.00'], resto = divmod(resto, 1000)
notas['5.00'], resto = divmod(resto, 500)
notas['2.00'], resto = divmod(resto, 200)
moedas['1.00'], resto = divmod(resto, 100)
moedas['0.50'], resto = divmod(resto, 50)
moedas['0.25'], resto = divmod(resto, 25)
moedas['0.10'], resto = divmod(resto, 10)
moedas['0.05'], resto = divmod(resto, 5)
moedas['0.01'] = resto

print('NOTAS:')
for nota, qtd in notas.items():
    print(f'{qtd:.0f} nota(s) de R$ {nota}')
print('MOEDAS:')
for moeda, qtd in moedas.items():
    print(f'{qtd:.0f} moeda(s) de R$ {moeda}')
