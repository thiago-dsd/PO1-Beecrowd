while True:
    try:
        entrada = input()
    except EOFError:
        break
    else:
        final = entrada.replace('@', 'a').replace('&', 'e').replace('!', 'i').replace('*', 'o').replace('#', 'u')
        print(final)
