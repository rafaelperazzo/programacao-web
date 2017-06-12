# -*- coding: utf-8 -*-
def pertence(a,b):
    cont=0
    for i in range (0,len(a)-1,1):
        if a[i] in b:
            cont=cont+1
    return cont

a=[]
qa=int(input('Tamanho de a:'))
for i in range (0,qa,1):
    valor=int(input('Valor:'))
    a.append(valor)
    
b=[]
qb=int(input('Tamanho de b:'))
for i in range (0,qb,1):
    valor=int(input('Valor:'))
    b.append(valor)

print(qa)
print(qb)
print(pertence(a,b))