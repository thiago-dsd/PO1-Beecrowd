m = 0
contador = 0
while m == 0:
    contador += 1
    total = int(input())
    if total == 0:
        m = 1
    else:
        print('Teste {}'.format(contador))
        cinq = total // 50
        dez = (total % 50) // 10
        cinco = (total % 50)%10 // 5
        um = ((total % 50)%10)%5
        print(cinq, dez, cinco, um)
        print('')

