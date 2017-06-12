# -*- coding: utf-8 -*-
n=int(input('Digite n:'))
p=int(input('Digite p:'))
i=0
cont=0
a=[]

for i in range(1,n+1,1):
    a=int(input('Digite a:'))
    b=int(input('Digite b:'))
    
    if (a+b)>=p:
        cont=cont+1
print(cont)
