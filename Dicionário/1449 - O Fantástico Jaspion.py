casos = int(input())
for _ in range (casos):
    dicionario = {}
    qntPalavras, qntLinhasMusica = input().split()
    qntPalavras, qntLinhasMusica = int(qntPalavras), int(qntLinhasMusica)
    for _ in range (qntPalavras):
        palavraAtual = input()
        dicionario[palavraAtual] = 'X'
    for _ in range (qntPalavras):
        tradPalavraAtual = input()
        dicionario
