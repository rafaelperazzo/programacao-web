# -*- coding: utf-8 -*-
for i in range (1000,9999,1): 
    raiz = 0
    primeiro_par=i//100
    segundo_par=i%100
    raiz=(primeiro_par+segundo_par)**(1/2)
    if raiz%1 == 0:
        print(i)
    