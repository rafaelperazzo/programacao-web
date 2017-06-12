# -*- coding: utf-8 -*-
n=int(input('Quantidedade de pessoas que passam na escada:'))
a=[]
for i in range(1,n+1,1):
    ins=int(input('%dºInstante:'%i))
    a.append(ins)
soma=0
for i in range(len(a)-1,0,-1):
    b=a[i]-a[i-1]
    soma=soma+b
t=soma+10
print(t)