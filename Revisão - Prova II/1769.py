while True:
    try:
        cpf = input().replace('.', '')
    except EOFError:
        break
    else:
        list_a, list_b = cpf.split('-')
        
        tmp_b1 = tmp_b2 = 0
        for k, v in enumerate(list_a):
            k += 1 # iniciar em 1
            v = int(v)
            tmp_b1 += k * v
            tmp_b2 += (9-k+1) * v
            
        b1 = tmp_b1 % 11
        if b1 == 10:
            b1 = 0
        b2 = tmp_b2 % 11
        if b2 == 10:
            b2 = 0
        
        if b1 == int(list_b[0]) and b2 == int(list_b[1]):
            print('CPF valido')
        else:
            print('CPF invalido')
