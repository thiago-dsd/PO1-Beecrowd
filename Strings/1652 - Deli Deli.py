irregulares = []
num_irr, num_entrada = input().split()
num_irr, num_entrada = int(num_irr), int(num_entrada)
#adicionando todas irregulares em uma lista
for i in range (0, num_irr):
    irr = input().split()
    irr[0] = str(irr[0])
    irr[1] = str(irr[1])
    irregulares.append(irr[0])
    irregulares.append(irr[1])
for x in range (0, num_entrada):
    palavra = input()
    #se a palavra pertencer a lista de irregulares
    if irregulares.count(palavra) == 1 or irregulares.count(palavra) == 2:
        #printe a palavra que vem em seguida, isto é, o plural da irregular
        print(irregulares[irregulares.index(palavra) + 1])
    #se a palavra não for irregular
    else:
        lista_palavra = []
        for c in range (0, len(palavra)):
            lista_palavra.append(palavra[c])
        #terminal em uma consoante seguida de y
        if lista_palavra[-1] == 'y' and lista_palavra[-2] in 'bcdfghjklmnpqrstvwxyz':
            lista_palavra[-1] = 'ies'
        elif lista_palavra[-1] == 'o' or lista_palavra[-1] == 's' or (lista_palavra[-2] == 'c' and lista_palavra[-1] == 'h') or (lista_palavra[-2] == 's' and lista_palavra[-1] == 'h') or lista_palavra[-1] == 'x':
            lista_palavra.append('es')
        else:
            lista_palavra.append('s')
        print(''.join(lista_palavra))
    

