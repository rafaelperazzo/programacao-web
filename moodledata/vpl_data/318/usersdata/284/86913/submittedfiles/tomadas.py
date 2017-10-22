# -*- coding: utf-8 -*-
import math

#COMECE SEU CODIGO AQUI
t1=int(input('digite quantiade de tomadas da regua1: '))
t2=int(input('digite quantiade de tomadas da regua2: '))
t3=int(input('digite quantiade de tomadas da regua3: '))
t4=int(input('digite quantiade de tomadas da regua4: '))
if t1<=0 or t2<=0 or t3<=0 or t4<=0:
    t1=int(input('digite quantiade de tomadas da regua1: '))
    t2=int(input('digite quantiade de tomadas da regua2: '))
    t3=int(input('digite quantiade de tomadas da regua3: '))
    t4=int(input('digite quantiade de tomadas da regua4: '))
else:
    v=t1+t2+t3+t4-3
    print(v)
    
    
    
