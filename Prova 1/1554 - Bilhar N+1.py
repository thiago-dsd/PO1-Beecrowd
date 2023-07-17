num = int(input())
#repetindo o numero de testes que serao feitos
for c in range (1, num+1):
    #perguntando o numero de bolas que havera no teste
    num_bolas = int(input())
    #estipulando um valor hipotetico de distancia, o qual e bem alto
    distancia_menor = 100000
    #repetindo o numero de tese que serao feitos com cada bola
    for s in range(1, num_bolas+2):
        #perguntando a posicao de cada bola
        x, y = input().split()
        x = int(x)
        y = int(y)
        #se estivermos falando da bola branca, armazenamos o valor dessa bola
        if s == 1:
            x_bolabranca = x
            y_bolabranca = y
        #se for alguma outra bola, calculamos a distancia dessa para a bola branca
        else:
            distancia = ((x_bolabranca - x)**2 + (y_bolabranca - y)**2)**(1/2)
        #se a distancia dessa bola para a bola branca ´e menor do que a distancia da bola menor essa bola se torna a bola com distancia menor
            if distancia < distancia_menor:
                distancia_menor = distancia
                bola_menor = s
    print(bola_menor-1)
        


