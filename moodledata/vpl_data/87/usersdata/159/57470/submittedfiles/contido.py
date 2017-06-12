# -*- coding: utf-8 -*-
def pertence(a):
    cont=0
    for i in range (0,len(a),1):
        for j in range (0,len(b),1):
            if a[i]==b[j]:
                cont=cont+1
    return cont

qa=int(input('Tamanho de a:'))
for i in range (0,qa,1):
    valor=float(input('Valor:'))
    a.append(valor)

qb=int(input('Tamanho de b:'))
for i in range (0,qb,1):
    valor=float(input('Valor:'))
    b.append(valor)

print(pertence(a))
print(pertence(b))