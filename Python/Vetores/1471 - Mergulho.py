while True:
    try:
        foi, retornou = input().split()
        foi = int(foi)
        retornou = int(retornou)
        #criando uma lista com os mergulhadores
        mergulhadores = input().split()
        for x in range (0, len(mergulhadores)):
            mergulhadores[x] = int(mergulhadores[x])
        #criando uma lista de zeros
        lista = []
        for c in range (0, foi+1):
            lista.append(0)
        #colocando um nos mergulhadores que voltaram
        for s in range (0, retornou):
            lista[mergulhadores[s]] = 1
        #print(lista)
        if foi - retornou != 0:
            for z in range (1, len(lista)):
                if lista[z] == 0:
                    print(z, end=' ')
            print('')    
        else:
            print('*')
    except EOFError:
        break

