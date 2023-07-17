contador = 0
while True:
    num_round = int(input())
    if num_round == 0:
        break
    contador += 1
    soma_aldo = soma_beto = 0
    for c in range (1, num_round + 1):
        a, b = input().split()
        a = int(a)
        b = int(b)
        soma_aldo += a
        soma_beto += b
    if soma_aldo > soma_beto:
        print(f'Teste {contador}')
        print('Aldo')
        print('')
    else:
        print(f'Teste {contador}')
        print('Beto')
        print('')
        

