# -*- coding: utf-8 -*-
a=[]
n=int(input('Digite a quantidade de elementos da lista: '))
for i in range(0,n,1):
    valor_a=float(input('Digite o elemento da lista: '))
    a.append(valor_a)
impar=0
par=0
conti=0
contp=0
for i in range(0,len(a),1):
    if (a[i]%2)!=0:
        impar=impar+a[i]
        conti=conti+1
    else:
        par=par+a[i]
        contp=contp+1
print(impar)
print(par)
print(conti)
print(contp)
print(a)
