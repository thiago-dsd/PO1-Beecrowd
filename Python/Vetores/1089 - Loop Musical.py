#os primeiros e os ultimos são sempre picos
#para ser um pico, os vizinhos devem ser menores
while True:
    num_picos = 0
    entrada = int(input())
    if entrada == 0:
        break
    lista = input().split()
    for i in range (0, len(lista)):
        lista[i] = int(lista[i])
        lista[i-1] = int(lista[i-1])
        lista[1] = int(lista[1])
        if i == 0:
            if lista[0] > lista[len(lista)-1] and lista[0] > lista[1]:
                num_picos += 1
            if lista[0] < lista[len(lista)-1] and lista[0] < lista[1]:
                num_picos += 1
        elif i == (len(lista)-1):
            if lista[len(lista)-1] > lista[len(lista)-2] and lista[len(lista)-1] > lista[0]:
                num_picos += 1
            if lista[len(lista)-1] < lista[len(lista)-2] and lista[len(lista)-1] < lista[0]:
                num_picos += 1
        else:
            lista[i+1] = int(lista[i+1])
            if lista[i] > lista[i-1] and lista[i] > lista[i+1]:
                num_picos += 1
            if lista[i] < lista[i-1] and lista[i] < lista[i+1]:
                num_picos += 1
    print(num_picos)


