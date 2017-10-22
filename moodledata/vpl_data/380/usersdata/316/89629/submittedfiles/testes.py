# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
x=int(input('x:'))
y=int(input('y:'))
mdc=1
if x>y:
    maior=x
else:
    maior=y
for i in range(1,maior):
    if x%i==0 and y%i==0:
        mdc=i
print(mdc)

x=int(input('x:'))
y=int(input('y:'))
import fractions
mdc=fractions.gcd(x,y)
print(mdc)
   
    
   

