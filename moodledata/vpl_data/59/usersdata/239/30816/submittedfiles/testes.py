# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
primo = int(input("digite o número: "))
for i in range(2,primo+1):
    if i != primo:
        i = primo % i
        if i==0:
            print("Não é primo")
        else:
            print("É Primo")
       
        


    
