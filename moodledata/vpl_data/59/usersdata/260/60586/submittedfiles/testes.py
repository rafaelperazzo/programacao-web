# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python

k=int(input("digite o número de repetições"))
soma=0
for i in range(0,k+1,1):
    soma=soma+(1**(i))*(4/(2*i+1))
print("soma.6f%" %soma)
