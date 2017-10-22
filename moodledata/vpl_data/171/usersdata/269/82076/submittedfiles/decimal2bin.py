# -*- coding: utf-8 -*-
binario=int(input('digite binario: '))
a=0
b=binario
while binario>0:
    binario=binario//10
    a=a+1


d=0
c=b
f=1
for i in range(0,a+1,1):
    e=b%10
    c=b//(10**f)
    d=e*(2**i)+d
    f=f+1
    
    
print(d)    
    

