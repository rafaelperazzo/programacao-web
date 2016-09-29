# -*- coding: utf-8 -*-
from __future__ import division

#Entrada

valor= ('Digite o valor do investimento:') 
taxa= ('Digite a taxa de invstimento:')

#Processamento

ano1= valor+(valor*taxa)
ano2= ano1+(ano1*taxa)
ano3= ano2+(ano2*taxa)
ano4= ano3+(ano3*taxa)
ano5= ano4+(ano4*taxa)
ano6= ano5+(ano5*taxa)
ano7= ano6+(ano6*taxa)
ano8= ano7+(ano7*taxa)
ano9= ano8+(ano8*taxa)
ano10= ano9+(ano9*taxa)

#Saida

print ('%.2f'%(ano1))
print ('%.2f'%(ano2))
print ('%.2f'%(ano3))
print ('%.2f'%(ano4))
print ('%.2f'%(ano5))
print ('%.2f'%(ano6))
print ('%.2f'%(ano7))
print ('%.2f'%(ano8))
print ('%.2f'%(ano9))
print ('%.2f'%(ano10)) 

