numLinguas = int(input())
linguasTraducao = {}
for i in range (numLinguas):
    lingua = input()
    traducao = input()
    linguasTraducao[lingua] = traducao
#print(linguasTraducao)

numCriancas = int(input())
criacasLingua = {}
for i in range (numCriancas):
    nome = input()
    linguaCrianca = input()
    print(nome)
    print(linguasTraducao[linguaCrianca])
    print()
    #criacasLingua[nome] = linguaCrianca
