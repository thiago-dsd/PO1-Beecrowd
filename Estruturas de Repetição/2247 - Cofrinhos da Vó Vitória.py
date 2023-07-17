ndepositos = int(input())
numero = 0
while ndepositos != 0:
    numero += 1
    print('Teste {}'.format(numero))
    SOMA = 0
    for c in range (0, ndepositos):
        recebidos = input()
        X, Y = recebidos.split()
        X = int(X)
        Y = int(Y)
        F = X-Y
        SOMA += F
        print(SOMA)
    print('')
    ndepositos = int(input())
