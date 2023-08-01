from string import ascii_uppercase as alfa

qtd_questoes = int(input())
desafort = input()
qtd_provas = int(input())

questoes = []
for _ in desafort:
    questoes.append([])

len_prova = len(desafort)

acertos = 0
for _ in range(qtd_provas):
    prova = input()
    for i in range(len_prova):
        if prova[i] != desafort[i]:
            questoes[i].append(prova[i])

for l in questoes:
    qtd = {x: 0 for x in alfa}
    
    for i in l:
        qtd[i] += 1
    
    mais_freq = 0
    for v in qtd.values():
        if v > mais_freq:
            mais_freq = v
    
    acertos += mais_freq

print(acertos)
