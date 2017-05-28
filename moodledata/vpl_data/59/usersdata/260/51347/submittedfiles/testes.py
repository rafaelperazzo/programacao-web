# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
n=int(input("n"))
a=n
z=n
c=0
cont=0
while a>0:
    a=a//10
    cont=cont+1
for i in range(1,cont+1,1):
    b=a//10**(cont-i)
    n=b*2**(cont-i)
    c=c+n