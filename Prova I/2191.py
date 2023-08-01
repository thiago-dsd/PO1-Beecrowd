# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

# Erros:
# Teste 3
#-1 4
#+1 8 -> erro no fim (contagem?)
 
# Teste 4
#-7 8
#+5 8 -> erro no começo (verificacoes?)

c = 0

while True:
    c += 1
    n = int(input())
    if n == 0:
        break
    else:
        melhor_saldo = saldo = melhor_com = melhor_fim = 0
        com = fim = 1
        for i in range(1, n+1):
            x, y = map(int, input().split())
            saldo = saldo + x - y  # x - favor, y - contra
            
            if saldo < 0:  # não compensará manter o período
                # inicia proximo periodo
                com = fim = i+1  # proximo i
                saldo = 0
            
            else:
                if i > com:  # se a partida atual ocorrer depois da partida do comeco do periodo
                    fim += 1
                if saldo > melhor_saldo:
                    melhor_saldo = saldo
                    melhor_com = com
                    melhor_fim = fim
                elif saldo == melhor_saldo:
                    if fim - com > melhor_fim - melhor_com:
                        melhor_com = com
                        melhor_fim = fim

        print('Teste', c)
        if melhor_saldo == 0:
            print('nenhum')
        else:
            print(melhor_com, melhor_fim)
        print()

