while True:
    try:
        pap = input()
        texto = []
        for c in range (0, len(pap)):
            texto.append(0)
            texto[c] = pap[c]
        for m in range (0, len(texto)):
            if texto[m] == '@':
                texto[m] = 'a'
            if texto[m] == '&':
                texto[m] = 'e'
            if texto[m] == '!':
                texto[m] = 'i'
            if texto[m] == '*':
                texto[m] = 'o'
            if texto[m] == '#':
                texto[m] = 'u'
        print(''.join(texto))
    except EOFError:
        break


