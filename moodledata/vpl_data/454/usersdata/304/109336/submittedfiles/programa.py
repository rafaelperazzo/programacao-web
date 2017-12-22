# -*- coding: utf-8 -*-
c = int(input('Digite o número de consultas ao estoque: '))
qntd = []
for i in range (0,c,1):
    qntd.append(int(input('Digite a consulta: ')))
for i in range (0,len(qntd),1):
    resp = 0
    if len(qntd)>0:
        resp = resp - 1
    else:
        resp = resp + 2
        qntd.append(1)
print (resp)
