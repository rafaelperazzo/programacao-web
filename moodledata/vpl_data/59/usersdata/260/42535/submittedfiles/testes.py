# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
px=float(input("digirte o valor de x em p"))
py=float(input("digirte o valor de y em p"))    
qx=float(input("digirte o valor de x em q"))
qy=float(input("digirte o valor de y em q"))
rx=float(input("digirte o valor de x em r"))
py=float(input("digirte o valor de y em r"))
for i in range (0,16,1):
    pxx=px+i*2**(-53)
    for j in range (0,16,1):
        pyy=py+j*2**(-53)
        print(x)+print(Y)
        
        det=(qx-pxx)*(ry-pyy)-(qy-pyy)*(rx-pxx)
        if det==0:
            print("sobre a reta")
        if det>0:
            print("à esquerda da reta")
        if det<0:
            print("à direita da reta")