# -*- coding: utf-8 -*-
import math

#COMECE SEU CODIGO AQUI
def tomadas():
    t1=int(input("Qual o número de tomadas da 1ª régua? "))
    t2=int(input("Qual o número de tomadas da 2ª régua? "))
    t3=int(input("Qual o número de tomadas da 3ª régua? "))
    t4=int(input("Qual o número de tomadas da 4ª régua? "))
    if t1==0 and t2==0 and t3==0 and t4==0:
        print ("0")
    elif t1>0 and t2==0 and t3==0 and t4==0:
        print (t1)
    elif t1>0 and t2>0 and t3==0 and t4==0:
        print (t1+t2-1)
    elif t1>0 and t2>0 and t3>0 and t4==0:
        print (t1+t2+t3-2)
    elif t1>0 and t2>0 and t3>0 and t4>0:
        print (t1+t2+t3+t4-3)
    
    
    
tomadas()
