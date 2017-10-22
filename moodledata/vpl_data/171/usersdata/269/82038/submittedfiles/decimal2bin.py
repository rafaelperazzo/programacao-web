# -*- coding: utf-8 -*-
binario=int(input('digite binario: '))
a=0
b=binario
while binario>0:
    binario=binario//10
    a=a+1

c=1
d=0
for i in range(0,a+1,1):
    decimal=b%10**c
    d=decimal*(2**i)+d
    c=c+1
print(d)    
    

