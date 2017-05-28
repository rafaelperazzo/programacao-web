# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
n=int(input("n"))
a=n
z=n
c=0
s=0
cont=0
while n>0:
    resto=n%2
    s=s+resto*10**(cont)
    n=n//2
    cont=cont+1
print(s)