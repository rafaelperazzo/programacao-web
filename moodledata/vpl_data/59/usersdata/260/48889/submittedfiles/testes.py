# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
anterior=0
b=0
for i in range(1,4,1):
    a=float(input("digite a quntidade de discos"))
    if anterior>a:
        maior=anterior
        c=b
        anterior=a
    else:
        maior=a
        c=i
        anterior=a
        b=i
print(c)