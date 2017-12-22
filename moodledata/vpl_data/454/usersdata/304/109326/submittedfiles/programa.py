# -*- coding: utf-8 -*-
c = int(input('Digite o número de consultas ao estoque: '))
qntd = []
for i in range (0,c,1):
    qntd.append(int(input('Digite a consulta: ')))
    resp = 0
    if len(qntd)>0:
        del qntd[i]
    else:
        resp = resp + 2
        qntd.append(i)
print (resp)
