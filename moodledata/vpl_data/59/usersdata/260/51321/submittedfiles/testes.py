# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
n=int(input("n"))
i=int(input("i"))
j=int(input("j"))
contador=0
for numero (1,i*j**n,1):
    if j%numero==i%numero:
        print(numero)
        contador=contador+1
        if contador ==n:
            break