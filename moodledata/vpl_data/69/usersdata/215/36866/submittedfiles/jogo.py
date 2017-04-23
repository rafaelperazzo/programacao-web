# -*- coding: utf-8 -*-
CV=int(input('q vitorias do cormengo'))
CE=int(input('q vitorias do cormengo'))
CS=int(input('q vitorias do cormengo'))
FV=int(input('q vitorias do cormengo'))
FE=int(input('q vitorias do cormengo'))
FS=int(input('q vitorias do cormengo'))
PC=(CV*3)+CE
PF=(FV*3)=FE
if PC>PF:
    print('c')
elif PF>PC:
    print('f')
else:
    if CS>FS:
        print('c')
    elif FS >CS:
        print ('f')
    else:
        print('=')