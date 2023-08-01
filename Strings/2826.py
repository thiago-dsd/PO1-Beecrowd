from string import ascii_lowercase as alfabeto


p1 = input()
p2 = input()

if len(p1) <= len(p2):
    menor = p1
    maior = p2
else:
    menor = p2
    maior = p1

ordem_existe = False
for i in range(len(menor)):
    p1_i = alfabeto.index(p1[i])
    p2_i = alfabeto.index(p2[i])
    
    if p1_i < p2_i:
        ordem = (p1, p2)
        ordem_existe = True
        break
    
    elif p2_i < p1_i:
        ordem = (p2, p1)
        ordem_existe = True
        break

if not ordem_existe:
    ordem = (menor, maior)

for p in ordem:
    print(p)
