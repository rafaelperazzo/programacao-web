# -*- coding: utf-8 -*-
    
n=int(input('digite n:'))
a=[]

for i in range(0,n,1):
    valor=float(input('digite um valor:'))
    a.append(valor)
soma1=0
soma2=0
for i in range(0,len(a),1):
    if i%2==0:
        soma1=soma1+1
    elif i%2==1:
        soma2=soma2+1
print(soma1)
print(soma2)



