# -*- coding: utf-8 -*-
c = int(input('Digite o número de consultas ao estoque: '))
qntd = []
for i in range (0,c,1):
    qntd.append(int(input('Digite: ')))
resp = 0
if qntd[i]>0:
    del qntd[i]
else:
    resp = resp + 2
    qntd.append(1)
print (resp)