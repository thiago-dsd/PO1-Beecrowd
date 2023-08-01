while True:
    try:
        hora, minuto = map(int, input().split(':'))
    except:
        break
    else:
        horas = [0, 0, 0, 0]  # 4 elementos (8, 4, 2, 1)
        minutos = [0, 0, 0, 0, 0, 0]  # 6 elementos (32, 16, 8, 4, 2, 1)
        
        horas[0], resto = divmod(hora, 8)
        horas[1], resto = divmod(resto, 4)
        horas[2], resto = divmod(resto, 2)
        horas[3] = resto
        
        minutos[0], resto = divmod(minuto, 32)  # minuto // 32, minuto % 32
        minutos[1], resto = divmod(resto, 16)
        minutos[2], resto = divmod(resto, 8)
        minutos[3], resto = divmod(resto, 4)
        minutos[4], resto = divmod(resto, 2)
        minutos[5] = resto
        
        bolinhas_hora = ['o' if x == 1 else ' ' for x in horas]
        bolinhas_minutos = ['o' if x == 1 else ' ' for x in minutos]
        
        print(
""" ____________________________________________
|                                            |
|    ____________________________________    |_
|   |                                    |   |_)
|   |   8         4         2         1  |   |
|   |                                    |   |
|   |   {}         {}         {}         {}  |   |
|   |                                    |   |
|   |                                    |   |
|   |   {}     {}     {}     {}     {}     {}  |   |
|   |                                    |   |
|   |   32    16    8     4     2     1  |   |_
|   |____________________________________|   |_)
|                                            |
|____________________________________________|""".format(*bolinhas_hora, *bolinhas_minutos))
        
        print()
