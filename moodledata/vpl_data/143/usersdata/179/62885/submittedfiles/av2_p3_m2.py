# -*- coding: utf-8 -*-
def degrais(a):
    menos=0
    degrau=0
    for i in range(0,len(a)-1,1):
        menos=(a[i]-a[i+1])
        if menos<0:
            menos=menos*(-1)
        if menos>degrau:
            degrau=menos
    return degrau
n=int(input('digite o valor de n :'))
b=[]
for i in range(0,n,1):
    numero=int(input('digite o numero :'))
    b.append(numero)
x=degrais(b)
x=int(input('digite o valor de  :'))
c=[]
for i in range(0,x,1):
    valor=int(input('digite o valor :'))
    c.append(valor)
print(c)    
