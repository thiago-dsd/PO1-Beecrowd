lista = []
while True:
    try:
        numRegistros = int(input())
        for k in range (numRegistros):
            registroAtual = int(input())
            lista.append(registroAtual)
    except EOFError:
        break
