# -*- coding: utf-8 -*-
n=int(input('valor de n: '))
a=[]
si=0
sp=0
conti=0
contp=0
for i in range(1,n+1,1):
    valor=int(input('digite o valor: '))
    a.append(valor)
for i in range(0,len(a),1):
    if lista[i]%2!=0:
        si=si+a[i]
        conti=conti+1
    else:
        sp=sp+a[i]
        contp=contp+1
print(si)        
print(sp)
print(conti)
print(contp)
print(a)