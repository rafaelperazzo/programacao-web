# -*- coding: utf-8 -*-
    
n=int(input('digite n:'))
a=[]

for i in range(0,n,1):
    valor=float(input('digite um valor:'))
    a.append(valor)
    
soma1=0
soma2=0
cont1=0
cont2=0
for i in range (0,len(a),1):
    if n%i==0:
        soma1=soma1+1
        cont1=cont1+1
        print(soma1,cont1)
    else:
        soma2=soma2+1
        cont2=cont2+1
print(soma2,cont2)
print(a)


