# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite a quantidade de elementos numéricos desejável: ' ))
a=[]
for i in range(0,n,1):
    a.append(int(input('Digite os valores: ')))
soma=0
med=sum(a)/len(a)
for i in range(0,n,1):
    soma+=(a[i]-med)**2
desv=((1/(n-1)*soma))**0.5
print(desv)
    

    

    
    
    
    
