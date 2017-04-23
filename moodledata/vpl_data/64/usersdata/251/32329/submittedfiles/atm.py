# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
valor = int (input('Insira o valor: '))
cedula = 0
resto = 0
resto1 = 0
resto2 = 0
resto3 = 0
resto4 = 0

if valor>=20:
    cedula = int (valor/20)
    print ('%d'%cedula)
    resto = (valor-(cedula*20))
else:
    print(0)
    resto = (valor-(cedula*20))
    
if resto>=10:
    cedula = int (resto/10)
    print ('%d'%cedula)
    resto1 = (resto-(cedula*10))
        
else:
    print (0)
    resto1 = resto
        
if resto1>=5:
    cedula = int (resto1/5)
    print ('%d'%cedula)
    resto2 = (resto1-(cedula*5))
            
else:
    print (0)
    resto2 = resto1
            
if resto2>=2:
    cedula = int (resto2/2)
    print ('%d'%cedula)
    resto3 = (resto2-(cedula*2))
    
else:
    print(0)
    resto3 = resto2
        
if resto3>=1:
    cedula = int (resto/1)
    print ('%d'%cedula)
    
else:
    print(0)
        
