lines = '`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;\'ZXCVBNM,./'

while True:
    try:
        entrada = input()
    except:
        break
    else:
        final = ''
        for i in entrada:
            if i == ' ':
                final += ' '
            else:
                final += lines[lines.index(i)-1]
                
        print(final)
