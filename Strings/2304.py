din_inicial, n = map(int, input().split())
players = {x: din_inicial for x in ('D', 'E', 'F')}

for _ in range(n):
    op, *_players, money = input().split()
    money = int(money)
    if op == 'C':
        players[_players[0]] -= money
    elif op == 'V':
        players[_players[0]] += money
    else:
        players[_players[0]] += money
        players[_players[1]] -= money

print(players['D'], players['E'], players['F'])
