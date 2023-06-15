N = int(input())
comidos = 0
maximo = 0
for i in range(0, N):
    entrada = list(input())
    #o comportamento é diferente para linhas pares e para linhas ímpares, por isso criamos esse IF
    if i%2 == 0:
        for j in range(0,N):
            #Se encontrar um "o" somamos mais um na quantidade de comida
            if entrada[j] == "o":
                comidos += 1
            elif entrada[j] == "A":
                #se encontrar um "A" a contagem zera, pois encontrou um monstro
                comidos = 0
            else:
                comidos += 0
            maximo = max(maximo, comidos)
    else:
        #o princípio é o mesmo para as linhas ímpares
        for j in range(0,N):
            if entrada[N-1-j] == "o":
                comidos += 1
            elif entrada[N-1-j] == "A":
                comidos = 0
            else:
                comidos += 0
            maximo = max(maximo, comidos)

print(maximo)







