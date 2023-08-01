# 3: terno
# 4: quadra
# 5: quina
# 6: sena
ganhou = ['terno', 'quadra', 'quina', 'sena']

flavinho = input().split()
sorteados = input().split()

acertos = 0 
for i in flavinho:
    if i in sorteados:
        acertos += 1
        
if acertos < 3:
    print('azar')
else:
    print(ganhou[acertos-3])
