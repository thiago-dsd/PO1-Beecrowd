v = int(input())
p = int(input())
#.se o valor das parcelas e rendondo, basa imprimir a divisao do total pelo numero de parcelas
if v % p == 0:
    for c in range (1, p+1):
        div = v/p
        print('{:.0f}'.format(div))
else:
    #do contrario e preciso estipular um valor fixo que sera pago todo mes
    fixo = v // p
    #o resto desse valor fixo deve ser pago no menor numero de parcelas possiveis, tendo essas um valor inteiro
    resto = v % p
    #encontrando o menor valor que pode ser pago
    num_fixo_inteiro = 0
    for c in range (p, 0, -1):
        if resto // c >= 1:
            fixo_inteiro = resto / c
            num_fixo_inteiro = resto / fixo_inteiro
            break
    num_fixo_inteiro = int(num_fixo_inteiro)
    for s in range (1, num_fixo_inteiro+1):
        print('{:.0f}'.format(fixo_inteiro + fixo))
    for s in range (1, (p - num_fixo_inteiro) + 1):
        print(fixo)

