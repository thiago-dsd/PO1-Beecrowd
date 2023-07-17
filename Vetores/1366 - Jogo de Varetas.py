while True:
    pares = 0
    num = int(input())
    if num == 0:
        break
    for c in range (0, num):
        comprimento, quantidade = input().split()
        comprimento, quantidade = int(comprimento), int(quantidade)
        pares += quantidade // 2
    print(pares // 2)
    


