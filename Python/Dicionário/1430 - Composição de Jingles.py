while True:
    identificadorDuracao = {'W': 64, 'H': 32, 'Q': 16, 'E': 8, 'S': 4, 'T': 2, 'X': 1}
    lista = input()
    if lista == '*':
        break
    else:
        lista = lista.split('/')
        contador = 0
        for k in range (0, len(lista)):
            somaDuracao = 0
            for m in range (len(lista[k])):
                if lista[k][m] in identificadorDuracao:
                    letra = lista[k][m]
                    somaDuracao += identificadorDuracao[letra]
            if somaDuracao == 64:
                contador += 1
        print(contador)

