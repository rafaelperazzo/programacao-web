# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de elementos da lista: '))
a=[]
qp=0
qi=0
sp=0
si=0
for i in range (1, n+1, 1):
    valor=float(input('Valor da lista: '))
    a.append(valor)
for j in range (0, len(a), 1):
    if (a[j]%2==0):
        qp=qp+1
        sp=sp+a[j]
    else:
        qi=qi+1
        si=si+a[j]
print(si)
print(sp)
print(qi)
print(qp)
print()
