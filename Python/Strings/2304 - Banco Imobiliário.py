inicial, operacao = input().split()
inicial, operacao = int(inicial), int(operacao)
Dalia = Elia = Fenix = inicial
for i in range (0, operacao):
    lista = input().split()
    #caso da compra ou venda
    if len(lista) == 3:
        lista[2] = int(lista[2])
        #operacao de compra
        if lista[0] == 'C':
            if lista[1] == 'D':
                Dalia -= lista[2]
            elif lista[1] == 'E':
                Elia -= lista[2]
            else:
                Fenix -= lista[2]
        #operacao de venda
        else:
            if lista[1] == 'D':
                Dalia += lista[2]
            elif lista[1] == 'E':
                Elia += lista[2]
            else:
                Fenix += lista[2]
    #caso do aluguel
    else:
        lista[3] = int(lista[3])
        #quem recebe o aluguel
        if lista[1] == 'D':
            Dalia += lista[3]
        elif lista[1] == 'E':
            Elia += lista[3]
        else:
            Fenix += lista[3]
        #quem mora de aluguel
        if lista[2] == 'D':
            Dalia -= lista[3]
        elif lista[2] == 'E':
            Elia -= lista[3]
        else:
            Fenix -= lista[3]
print("{} {} {}".format(Dalia, Elia, Fenix))

