# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de termos : '))
a=[]
soma=0
for i in range(0,n,1):
    valor=float(input('Digite o termo: '))
    a.append(valor)
    soma=soma + valor
med=soma/len(a)
print(a[0])
print(a[n])
print(med)
print(a)



