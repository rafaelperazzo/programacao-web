# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python

x=int(input("digite o número de repetições: "))
soma=0
i=0
E=0
if x<=1 and x>=0:
    while E<0.0001:
        soma=soma_anterior=soma
        soma=soma+((-1)**(i+1))*((x**(i+1))/(i+1))
        E=soma-soma_anterior
        i=i+1
    print(soma)
