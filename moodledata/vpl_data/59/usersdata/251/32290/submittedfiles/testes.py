# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
valor = int (input('Insira o valor: '))
cedula = 0
resto = 0

if valor>=20:
        cedula = int (valor/20)
        print ('%d'%cedula)
        resto = (valor-(cedula*20))
        
        
if resto>=10:
    cedula = int (resto/10)
    print ('%d'%cedula)
    resto1 = (resto-(cedula*10))
            
        
if resto1>=5:
    cedula = int (resto1/5)
    print ('%d'%cedula)
    resto2 = (resto1-(cedula*5))
                
            
if resto2>=2:
    cedula = int (resto2/2)
    print ('%d'%cedula)
    resto3 = (resto2-(cedula*2))
                    
if resto3>=1:    
    cedula = int (resto3/1)
    print ('%d'%cedula)
    resto4 = (resto3-(cedula*1))
    
    