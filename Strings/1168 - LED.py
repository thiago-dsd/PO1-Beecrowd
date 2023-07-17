testes = int(input())
led = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6, 0]
for c in range (0, testes):
    qnt_led = 0
    num = input()
    for s in range (0, len(num)):
        caso = int(num[s])
        qnt_led += led[caso]
    print('{} leds'.format(qnt_led))
        
        

