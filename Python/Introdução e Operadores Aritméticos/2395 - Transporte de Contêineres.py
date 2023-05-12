cont = input()
nav = input()
LC, CC, AC = cont.split()
LN, CN, AN = nav.split()
LC = int(LC)
CC = int(CC)
AC = int(AC)
LN = int(LN)
CN = int(CN)
AN = int(AN)
ql = LN // LC
qc = CN // CC
qa = AN // AC
print('{}'.format(ql*qc*qa))

