letra = input().strip()
texto = input().split()

palavras_c_letra = 0
tot_palavras = len(texto)

for palavra in texto:
    if letra in palavra:
        palavras_c_letra += 1

porcentagem = (palavras_c_letra/tot_palavras) * 100
print(f'{porcentagem:.1f}')
