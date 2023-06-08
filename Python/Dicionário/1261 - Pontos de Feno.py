dicionario = {}
qntPalavras, cargos = input().split()
qntPalavras, cargos = int(qntPalavras), int(cargos)
for _ in range (qntPalavras):
    atualPalavra, valorPalavra = input().split()
    valorPalavra = int(valorPalavra)
    dicionario[atualPalavra] = valorPalavra
for _ in range (cargos):
    somaValor = 0
    listaPalavrasCargos = input().split()
    for k in range (len(listaPalavrasCargos)):
        if listaPalavrasCargos[k] == ".":
            break
        if listaPalavrasCargos[k] in dicionario:
            somaValor += dicionario[listaPalavrasCargos[k]]   
    print(somaValor)

