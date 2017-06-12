# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
n=int(input("n:"))
anterior=0.5
cont=0
for i in range(1,n+1,1):
    num=int(input("num:"))
    if num==anterior:
        cont=cont+1
    anterior=num
print(cont)
