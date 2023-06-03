num = int(input())
for c in range (0, num):
    lista = []
    palavras = input().split()
    if len(palavras[0]) != len(palavras[1]):
        #sabendo qual e a maior palavra e qual e a menor
        if len(palavras[0]) > len(palavras[1]):
            palavra_maior = len(palavras[0])
            str_palavra_maior = palavras[0]
            palavra_menor = len(palavras[1])
            str_palavra_menor = palavras[1]
        elif len(palavras[0]) < len(palavras[1]):
            palavra_maior = len(palavras[1])
            str_palavra_maior = palavras[1]
            palavra_menor = len(palavras[0])
            str_palavra_menor = palavras[0]
        else:
            palavra_maior = palavra_menor = len(palavras[0])
        #determinando a quantidade de caracteres alternados
        alternados = palavra_menor
        if len(palavras[0]) < len(palavras[1]):
            #adicionando os caracteres alternados
            for s in range(0, alternados):
                lista.append(str_palavra_menor[s])
                lista.append(str_palavra_maior[s])
            #imprimindo os caracteres nao alternados
            for t in range(alternados, palavra_maior):
                lista.append(str_palavra_maior[t])
        else:
            for s in range(0, alternados):
                lista.append(str_palavra_maior[s])
                lista.append(str_palavra_menor[s])
            #imprimindo os caracteres nao alternados
            for t in range(alternados, palavra_maior):
                lista.append(str_palavra_maior[t])
        #print(lista)
        #imprimindo caracteres da lista
        print(''.join(lista))
    else:
        for z in range (0, len(palavras[0])):
            palavra0 = palavras[0]
            palavra1 = palavras[1]
            lista.append(palavra0[z])
            lista.append(palavra1[z])
        print(''.join(lista))

