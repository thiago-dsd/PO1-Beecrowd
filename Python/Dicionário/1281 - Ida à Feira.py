numCompras = int(input())
for _ in range (numCompras):
    totalCompra = 0
    dicionario = {}
    numItems = int(input())
    for l in range (numItems):
        fruta, preco = input().split()
        dicionario[fruta] = float(preco)
    compraNumeros = int(input())
    for m in range (compraNumeros):
        frutaAtual, qntCompra = input().split()
        totalCompra += dicionario[frutaAtual]*float(qntCompra)
    print("R$ {:.2f}".format(totalCompra))
