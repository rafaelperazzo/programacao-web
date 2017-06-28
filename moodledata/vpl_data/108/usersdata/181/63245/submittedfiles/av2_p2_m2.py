# -*- coding: utf-8 -*-
a=[]
n=int(input('digite n:'))
for i in range (0,n,1):
     valor=int(input('digite o valor:'))
     a.append(valor)
    
entra=int(input('entra:'))
sai=int(input('sai:'))
x=0
for i in range (entra,sai+1,1):
    x=x+a[i]
print(x)    

