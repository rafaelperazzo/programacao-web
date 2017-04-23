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
            resto = (resto-(cedula*10))
            
        
            if resto>=5:
                cedula = int (resto/5)
                print ('%d'%cedula)
                resto = (resto-(cedula*5))
                
            
                if resto>=2:
                    cedula = int (resto/2)
                    print ('%d'%cedula)
                    resto = (resto-(cedula*2))
                    
                    if resto>=1:    
                        cedula = int (resto/1)
                        print ('%d'%cedula)
                        resto = (resto-(cedula*1))
    
    