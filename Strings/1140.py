while True:
    a = input()
    if a == '*':
        break
    else:
        a = a.split()
        letra = a[0][0].lower()  # inicial da primeira palavra
        for palavra in a:
            if palavra[0].lower() != letra:
                print('N')
                break
        else:
            print('Y')
