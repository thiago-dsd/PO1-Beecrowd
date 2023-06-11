while True:
    try:
        #cpf válido se SOMADIGITOS % 11 = 0
        #while True:
        resultado = False
        digitos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        cpf = input()
        #colocando o cpf na lista de dígitos
        digitos[1] = int(cpf[0])
        digitos[2] = int(cpf[1])
        digitos[3] = int(cpf[2])
        digitos[4] = int(cpf[4])
        digitos[5] = int(cpf[5])
        digitos[6] = int(cpf[6])
        digitos[7] = int(cpf[8])
        digitos[8] = int(cpf[9])
        digitos[9] = int(cpf[10])
        digitos[10] = int(cpf[12])
        digitos[11] = int(cpf[13])
        
        teste1 = (((digitos[1]*1) + (digitos[2]*2) + (digitos[3]*3) + (digitos[4]*4) + (digitos[5]*5) + (digitos[6]*6) + (digitos[7]*7) + (digitos[8]*8) + (digitos[9]*9)) % 11)
        if teste1 == 10:
            teste1 = 0
        teste2 = (((digitos[1]*9) + (digitos[2]*8) + (digitos[3]*7) + (digitos[4]*6) + (digitos[5]*5) + (digitos[6]*4) + (digitos[7]*3) + (digitos[8]*2) + (digitos[9]*1)) % 11)
        if teste2 == 10:
            teste2 = 0
            
            
            
        if digitos[10] == teste1 and digitos[11] == teste2:
            resultado = True
        else:
            resultado = False
            
            
            
            
        if resultado == True:
            print('CPF valido')
        else:
            print('CPF invalido')
    except EOFError:
        break



