contador = 1
num_parcial = 0
num_operacoes = 0
while num_operacoes != -1:
    num_operacoes = int(input())
    if num_operacoes != -1:	
        num_quadrados = 2
        for c in range (0, num_operacoes):
            num_parcial = 2**c
            num_quadrados += num_parcial
        print('Teste {}'.format(contador))
        print(num_quadrados**2)
        contador += 1
        print('')
        
