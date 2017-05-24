# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
b=0
for i in range(1,5,1):
    a=float(input("digite a quntidade de discos"))
    if b>a:
        maior=b
        c=i
    else:
        maior=a
        c=i
    b=a
print(c)