# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
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
        
        
    if resto>=10:
        cedula = int (resto/10)
        print ('%d'%cedula)
        resto1 = (resto-(cedula*10))
            
        
        