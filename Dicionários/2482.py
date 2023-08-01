n = int(input())

dados = {}
for _ in range(n):
    lang = input()
    msg = input()
    dados[lang] = msg
    
m = int(input())

for _ in range(m):
    nome = input()
    lang = input()
    print(nome)
    print(dados[lang])
    print()
