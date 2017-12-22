# -*- coding: utf-8 -*-
ano=n
cont1=80000
cont2=200000
taxa1=0.03
taxa2=0.015

while cont1 == cont2 or cont1> cont2:
    for i in range(0,n,1):
        cont1= (cont1*0.03) + cont1
        cont2= (cont2*0.015) + cont2
else:
    print(n)