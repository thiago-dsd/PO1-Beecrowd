# achar a interseccao da linha e coluna erradas
# duas colunas / duas linhas iguais: soma correta
# verificar as tres primeiras linhas (alguma pode ser a errada)

n = int(input())

a1 = a2 = a3 = 0
m = []
for i in range(n):
    linha = [int(x) for x in input().split()]
    m.append(linha)
    
    # codigo feio abaixo
    if i == 0:
        a0 = sum(linha)
    elif i == 1:
        a1 = sum(linha)
    elif i == 2:
        a2 = sum(linha)

# pega o valor correto    
if a0 == a1 or a0 == a2:
    cor = a0
elif a1 == a2:
    cor = a1

for i in range(n): # linhas
    soma = sum(m[i])
    if soma != cor:
        lin_er = i

for j in range(n):
    soma = 0
    for i in range(n):
        soma += m[i][j]
    if soma != cor:
        col_er = j

n_err = m[lin_er][col_er]

soma_l = sum(m[lin_er])

n_cer = abs(soma_l - cor - n_err)

print(n_cer, n_err)
