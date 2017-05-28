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
    resto=n%10
    s=s+resto*2**(cont)
    n=n//10
    cont=cont+1
print(s)