# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
n=int(input("n:"))
anterior=0.5
cont=0
for i in range(1,n+1,1):
    num=int(input("num:"))
    if anterior<num:
        cont=cont+1
    anterior=num
    else:
        parcial=cont
        if parcial>cont_max:
            cont_max=parcial
print(cont_max)
