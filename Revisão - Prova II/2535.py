while True:
    try:
        n = int(input())
    except EOFError:
        break
    else:
        validos = 0
        for i in range(n):
            especie = input().split()
            raca = input()
            nome = input().split()
            input()
            
            valido = False
            if especie[0] == 'cachorro':
                if len(nome) > 1:
                    for palavra in nome:
                        if palavra[0] == raca[0]:
                            valido = True
            
            if valido:
                validos += 1
    
        print(validos)
