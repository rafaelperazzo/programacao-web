# -*- coding: utf-8 -*-
x= int(input('Digite um valor com 8 casas decimais: '))
y= 10000000
z= 100000000
soma= 0

while (True):
   if x<y:
       print('NAO SEI')
       break
   if x>z:
       print('NAO SEI')
       break
while (x>0):
   resto= x%10
   x=x//10
   soma= soma+resto
print(x)
        
   
   