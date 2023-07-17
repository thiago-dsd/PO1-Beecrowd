somador = 0
lado_quadrados = 1
while lado_quadrados != 0:
    lado_quadrados = int(input())
    if lado_quadrados != 0:
        for c in range (1, lado_quadrados + 1):
            num_atual = c**2
            somador += num_atual
        print(somador)
        somador = 0


