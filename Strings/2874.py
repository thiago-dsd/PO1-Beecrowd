while True:
    try:
        n = int(input())
    except EOFError:
        break
    else:
        final = ''
        
        for _ in range(n):
            p = input()
            base_10 = int('0b'+p, 2)
            final += chr(base_10)
            
        print(final)
