# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

a=int(input('Digite a: '))
b=int(input('Digite b: '))
q=int(input('Digite q: '))    
    
c=0
i=2
while (i<=q):
    if (a%i==0) and (b%i==0):
        c=c+i
    i=i+1
print(c)

    

