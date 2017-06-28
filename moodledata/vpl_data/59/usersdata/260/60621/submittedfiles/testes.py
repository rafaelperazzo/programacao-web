# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python

x=float(input("digite o número do arcotangente : "))
soma=0
i=1
E=10000
if x<=1 and x>=0:
    while E>0.000000001:
        soma_anterior=soma
        soma=soma+((-1)**(i-1))*((x**(i))/(i))
        E=((x**(i))/(i))
        i=i+1
    print("sua arcotangente será: %.10f" %soma)
