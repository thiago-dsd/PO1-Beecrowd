n, m = input().split()
n = int(n)
m = int(m)
#criando uma lista o número de partidas que o jogador fez gol
#inicialmente eles não marcaram em nenhuma partida, já que nenhuma partida foi analisada
QntJogosEmQueMarcou = [0] * n
#analisando partidas:
for k in range (0, n):
    partidas = input().split()
    for x in range (0, m):
        #se o jogador marcou mais que 1 gol da partida
        if int(partidas[x]) >= 1: 
            QntJogosEmQueMarcou[k] += 1 #então ele marcou naquele jogo
JogQueMarcaramTodaPartida = 0
for k in range (0, n):
    if QntJogosEmQueMarcou[k] == m:
        JogQueMarcaramTodaPartida += 1
print(JogQueMarcaramTodaPartida)