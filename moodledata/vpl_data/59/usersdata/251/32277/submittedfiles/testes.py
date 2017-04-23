# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
valor = int (input('Insira o valor: '))
cedula = 0
resto = 0

if valor>=20:
        cedula = int (valor/20)
        print ('%d'%cedula)
        resto = (valor-(cedula*20))
        print ('%d'%resto)
    
    