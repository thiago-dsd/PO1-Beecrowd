dias = int(input())
anos = dias // 365
meses = (dias % 365) // 30
d = dias - (365*anos + 30*meses)
print('{} ano(s)'.format(anos))
print('{} mes(es)'.format(meses))
print('{} dia(s)'.format(d))
