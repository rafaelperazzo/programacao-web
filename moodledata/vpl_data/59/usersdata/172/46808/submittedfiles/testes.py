# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('n:'))
c=1
while c<=n:
    x=float(input('x'))
    y=float(input('y'))
    x1=x**2
    y1=y**2
    if x>=0 and y>=0 and x1+y1<=1:
        print('SIM')
    else:
        print('NÃO')
    c=c+1    

        
