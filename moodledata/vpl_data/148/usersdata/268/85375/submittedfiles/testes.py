# -*- coding: utf-8 -*-
n=float(input('Digite o valor do investimento : '))
t=float(input('Digite o valor da taxa : '))
t1=t/100
cont=0

while(cont<10):
    valor= n + n*t1
    print(valor)
    n=n+n*t1
    cont=cont+1
