while True:
    try:
        n, m = [int(x) for x in input().split()]
    except EOFError:
        break
    else:
        tot = 0
        for _ in range(n):
            tot += sum([int(x) for x in input().split()])
        
        sacas, litros = divmod(tot, 60)
        print(f'{sacas} saca(s) e {litros} litro(s)')
