# -*- coding: utf-8 -*-
alunosidade=[]
alunosaltura=[]
while (True):
    id = int(input('Digite sua idade: '))
    h = float(input('Digite sua altura: '))
    if id>18 and h>0:
        alunosidade.append(id)
        alunosaltura.append(h)
    elif id<18:
        id = int(input('Digite sua idade: '))
        alunosidade.append(id)
        alunosaltura.append(h)
    elif h<0:
        h = float(input('Digite sua altura: '))
        alunosidade.append(id)
        alunosaltura.append(h)
    
print(alunosidade)
print(alunosaltura)
    

