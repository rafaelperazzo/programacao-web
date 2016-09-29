# -*- coding: utf-8 -*-
from __future__ import division

#ENTRADA:
Inv=input ('Digite o valor do investimento:') 
taxa=input ('Digite a taxa em casas decimais:')

Inv1= Inv+(taxa*Inv)
Inv2= Inv1+(taxa*Inv1)
Inv3= Inv2+(taxa*Inv2)
Inv4= Inv3+(taxa*Inv3)
Inv5= Inv4+(taxa*Inv4)
Inv6= Inv5+(taxa*Inv5)
Inv7= Inv6+(taxa*Inv6)
Inv8= Inv7+(taxa*Inv7)
Inv9= Inv8+(taxa*Inv8)
Inv10= Inv9+(taxa*Inv9)

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