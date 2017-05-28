# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
n=int(input("n"))
i=int(input("i"))
j=int(input("j"))
contador=0
for numero in range(0,n+1,1):
    if numero % i == 0 or numero % j == 0:
        print(numero)
        contador=contador+1
        if contador==n+1:
            break