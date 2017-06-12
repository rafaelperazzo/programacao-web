# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
n=int(input("n:"))
anterior=n+1
cont=0
cont_max=0
for i in range(1,n+1,1):
    num=int(input("num:"))
    if anterior<num:
        cont=cont+1
        print(cont)
    else:
        parcial=cont
        cont=0
        if parcial>cont_max:
            cont_max=parcial
    anterior=num
print(cont_max)
