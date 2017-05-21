# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
px=float(input("digirte o valor de x em p"))
py=float(input("digirte o valor de y em p"))    
qx=float(input("digirte o valor de x em q"))
qy=float(input("digirte o valor de y em q"))
rx=float(input("digirte o valor de x em r"))
ry=float(input("digirte o valor de y em r"))
contador=0
for i in range (0,15,1):
    pxx=px+i*2**(-53)
    for j in range (0,15,1):
        pyy=py+j*2**(-53)
        contador=contador+1
        det=(qx-pxx)*(ry-pyy)-(qy-pyy)*(rx-pxx)
        if det==0:
            print("sobre a reta")
            l=[pxx,pyy]
        if det>0:
            print("à esquerda da reta")
            t=[pxx,pyy]
        if det<0:
            print("à direita da reta")
            e=[pxx,pyy]
print(l)
print(t)
print(e)
print(contador)

