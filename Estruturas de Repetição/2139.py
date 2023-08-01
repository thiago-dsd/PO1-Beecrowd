# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
while True:
    try:
        data = map(int, input().split())
    except EOFError:
        break
    else:
        mes, dia = data
        if mes == 12:
            if dia == 24:
                print('E vespera de natal!')
                continue
            elif dia == 25:
                print('E natal!')
                continue
            elif dia > 25:
                print('Ja passou!')
                continue
            
        natal = 360  # 366 dias -> 366: 31/12; 31-25=6 -> 366-6=360: 25/12
        atual = 0
        if mes > 1:
            atual += 1
        if mes > 2:  # bissexto
            atual -= 1  
        if mes > 3:
            atual += 1
        if mes > 5:
            atual += 1
        if mes > 7:
            atual += 1
        if mes > 8:
            atual += 1
        if mes > 10:  
            atual += 1
        
        atual += (mes-1)*30 + dia
        print(f'Faltam {natal - atual} dias para o natal!')
