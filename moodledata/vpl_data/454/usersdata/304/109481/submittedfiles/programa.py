# -*- coding: utf-8 -*-
c = int(input('Digite o número de consultas ao estoque: '))
qntd = []
for i in range (0,c,1):
    qntd.append(int(input('Digite a consulta: ')))
    resp = 0
    if qntd[i]>0:
        qntd[i] = qntd[i] - 1
    else:
        resp = resp + 2
        qntd[i] = qntd[i] + 1
print (resp)

