# -*- coding: utf-8 -*-
num=int(input('Digite a quantidade de elementos da lista:'))
a=[]
qpar=0
qimp=0
somapar=0
somaimp=0
for i in range (1 , num+1, 1 ):
    valor=int(input('Valor da lista:'))
    a.append(valor)
for j in range (0, len(a), 1):
    if (a[j]%2==0):
        qpar=qpar+1
        somapar=somapar+a[j]
    else:
        qimpar=qimpar+1
        somaimp=somaimp+a[j]
print(somaimp)
print(somapar)
print(qimp)
print(qpar)
print(a)


