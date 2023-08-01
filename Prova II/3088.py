while True:
    try:
        entrada = input()
    except EOFError:
        break
    else:
        final = ''
        for i in range(len(entrada)-1):
            if entrada[i+1] in (',', '.') and entrada[i] == ' ':
                continue
            else:
                final += entrada[i]
        final += entrada[-1]
        
    print(final)
