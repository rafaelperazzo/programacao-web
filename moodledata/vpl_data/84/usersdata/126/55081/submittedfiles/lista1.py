# -*- coding: utf-8 -*-


n=int(input('digite o numero de elementos da lista:'))
a=[]
i=0
soma1=0
soma2=0
cont1=0
cont2=0
for i in range(1,n+1,1):
    m=int(input('digite um valor:'))
    a.append(m)
    i=i+1
for i in range(0,len(a),1):
    if a[i]%2==1:
        soma1=soma1+a[i]
        cont1=cont1+1
    elif a[i]%2==0:
        soma2=soma2+a[i]
        cont2=cont2+1
print(soma1)
print(soma2)
print(cont1)
print(cont2)
print(a)
        



    
    
