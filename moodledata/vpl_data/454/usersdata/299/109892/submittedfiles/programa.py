# -*- coding: utf-8 -*-
n=int(input(''))
tacos=[]
for i in range(0,n,1):
    tacos.append(int(input('')))
x=sorted(tacos)
cont=0
for i in range(1,n,1):
    if x[i-1]==x[i]:
        cont+=1
print((len(x)-cont)*2)