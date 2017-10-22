# -*- coding: utf-8 -*-
import math

#COMECE SEU CODIGO AQUI

for i in range(1,5,1) :
 
    while (True):
    
        t=int(input("Digite o valor de tomadas da régua %d, por gentileza:" %i))
        if (t>0):
             break
    if i==4:
        soma=soma*t
        print ("%d"%soma)
    else:
         soma = soma*(t-1)



    
    

#t2=int( input("Digite o valor de tomadas na segunda régua, por gentileza:"))
#t3=int(input("Digite o valor de tomadas na terceira régua, por gentileza:"))
#t4=int(input("Digite o valor de tomadas na quarta régua, por gentileza:"))


    
 

