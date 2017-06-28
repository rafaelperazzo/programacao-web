# -*- coding: utf-8 -*-
n=int(input('digite n:'))
a=[]
for i in range(1,n+1,1):
    valor=int(input('digite o valor:'))
    a.append(valor)
soma=0
soma1=0
cont=0
cont1=0
for i in range(0,len(a),1):
    if a[i]%2!=0:
        cont=cont+1
        soma=soma+a[i]
    else:
        cont1=cont1+1
        soma1=soma1+a[i]
print(soma)
print(soma1)
print(cont)
print(cont1)
print(a)

