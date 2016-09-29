# -*- coding: utf-8 -*-
from __future__ import division

#ENTRADA:
Inv=input ('Digite o valor do investimento:') 
taxa=input ('Digite a taxa em casas decimais:')

Inv1= Inv+(taxa*Inv)
Inv2= Inv+(taxa*Inv1)
Inv3= Inv+(taxa*Inv2)
Inv4= Inv+(taxa*Inv3)
Inv5= Inv+(taxa*Inv4)
Inv6= Inv+(taxa*Inv5)
Inv7= Inv+(taxa*Inv6)
Inv8= Inv+(taxa*Inv7)
Inv9= Inv+(taxa*Inv8)
Inv10= Inv+(taxa*Inv9)

print ('%.2f' %Inv1)
print ('%.2f' %Inv2)
print ('%.2f' %Inv3)
print ('%.2f' %Inv4)
print ('%.2f' %Inv5)
print ('%.2f' %Inv6)
print ('%.2f' %Inv7)
print ('%.2f' %Inv8)
print ('%.2f' %Inv9)
print ('%.2f' %Inv10)