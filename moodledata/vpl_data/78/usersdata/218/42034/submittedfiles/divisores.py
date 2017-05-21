# -*- coding: utf-8 -*-
import math
n=int(input('digite o valor de multiplos n:'))
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
ia=1
ib=1
contador=0
mua=0
mub=0
while contador<n:
   mua=a*ia
   mub=b*ib
   if mua<mub:
        print(mua)
        ia=ia+1
        
   elif mub<mua:
        print(mub)
        ib=ib+1
   else:
        print(mua)
        ia=ia+1
        ib=ib+1
   cont=cont+1    