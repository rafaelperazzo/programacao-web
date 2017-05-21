# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
px=float(input("digirte o valor de x em p"))
py=float(input("digirte o valor de y em p"))    
qx=float(input("digirte o valor de x em q"))
qy=float(input("digirte o valor de y em q"))
rx=float(input("digirte o valor de x em r"))
py=float(input("digirte o valor de y em r"))
det=(qx-px)*(ry-py)-(qy-py)*(rx-px)
if det==0:
    print("sobre a reta")
if det>0:
    print("à esquerda da reta")
if det<0:
    print("à direita da reta")