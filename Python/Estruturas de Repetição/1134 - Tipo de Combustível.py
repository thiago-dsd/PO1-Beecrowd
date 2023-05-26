conta = 0
contg = 0
contd = 0
n = int(input())
while n != 4:
    if n == 1:
        conta += 1
        n = int(input())
    elif n == 2:
        contg += 1 
        n = int(input())
    elif n == 3:
        contd += 1
        n = int(input())
    else:
        n = int(input())
print('MUITO OBRIGADO')
print('Alcool: {}'.format(conta))
print('Gasolina: {}'.format(contg))
print('Diesel: {}'.format(contd))

