s = int(input())
horas = s // 3600
minutos = (s % 3600) // 60
segundos = s - (3600*horas + 60*minutos)
print('{}:{}:{}'.format(horas, minutos, segundos))

