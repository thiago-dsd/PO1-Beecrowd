while True:
    try:
        n = int(input())
        lista = [0, 0, 0]
        for _ in range (n):
            numero, curso = input().split()
            if curso == "EPR":
                lista[0] += 1
            elif curso == "EHD":
                lista[1] += 1
            else:
                lista[2] += 1
        print("EPR: {}".format(lista[0]))
        print("EHD: {}".format(lista[1]))
        print("INTRUSOS: {}".format(lista[2]))
        lista = [0, 0, 0]
    except EOFError:
        break


