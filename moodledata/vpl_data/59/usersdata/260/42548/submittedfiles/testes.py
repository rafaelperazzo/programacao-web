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
lx=[]
tx=[]
ex=[]
ly=[]
ty=[]
ey=[]
for i in range (0,15,1):
    pxx=px+i
    for j in range (0,15,1):
        pyy=py+j
        det=(qx-pxx)*(ry-pyy)-(qy-pyy)*(rx-pxx)
        if det==0:
            print("sobre a reta")
            lx.append(pxx)
            ly.append(pyy)
        if det>0:
            print("à esquerda da reta")
            tx.append(pxx)
            ty.append(pyy)
        if det<0:
            print("à direita da reta")
            ex.append(pxx)
            ey.append(pyy)
print(lx,ly)
print(tx,ty)
print(ex,ey)


