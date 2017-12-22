# -*- coding: utf-8 -*-
n=0
cont1=80000
cont2=200000
taxa1=0.03
taxa2=0.015

while cont1 == cont2 or cont1> cont2:
        cont1= (cont1*0.03) + cont1
        cont2= (cont2*0.015) + cont2
        n+=1
else:
    print(n)