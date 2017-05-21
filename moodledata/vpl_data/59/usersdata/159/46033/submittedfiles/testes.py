# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=int(input('Digite a:'))
b=int(input('Digite b:'))
if a>=b:
    n=b
else:
    n=a
for i in range (1,n+1,1):
    if a%i==0 and b%i==0:
        divisor=i
print(divisor)        
 

    