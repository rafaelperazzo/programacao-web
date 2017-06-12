# -*- coding: utf-8 -*-
n=int(input('Digite um numero:'))
cont=0

while n>=0:
    if (n%10)==0:
        cont=cont+1
        n=n//10
    else:
        cont=cont+1
        n=n//10
    break
print(cont)
    
    
