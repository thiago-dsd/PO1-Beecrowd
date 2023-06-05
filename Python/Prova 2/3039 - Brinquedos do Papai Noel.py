num = int(input())
#perguntando a quantidade de crianças
carrinhos = bonecas = 0
for _ in range (0, num):
    nome, sexo = input().split()
    #se o sexo for M é homem, logo é preciso um carrinho
    #se o sexo for F é mulher, logo é uma boneca
    if sexo == 'M':
        carrinhos += 1
    if sexo == 'F':
        bonecas += 1
print('{} carrinhos'.format(carrinhos))
print('{} bonecas'.format(bonecas))

