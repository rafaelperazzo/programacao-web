# -*- coding: utf-8 -*-
n= int(input('Digite o valor de n:'))
a=[]
cont=0
for i in range (0,n,1):
    t= int(input('Digite o valor de t:'))
    a.append(t)

for i in range (1,len(a),1):
    soma= abs(a[i-1]-a[i])
    if soma>cont:
        cont=soma
        
print(cont)