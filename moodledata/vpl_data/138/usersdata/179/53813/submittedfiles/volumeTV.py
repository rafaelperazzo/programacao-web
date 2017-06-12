 -*- coding: utf-8 -*-
 v=int(input('digite o valor inicial do volume :'))
 t=int(input('digite o valor de trocas do volume :'))
 vf=v
 for i in range(1,t+1,1):
     tr=int(input('digite as trocas de volumes :'))
     if 0>=(vf+tr)<=100:
        vf=vf+tr
    elif vf+tr>=100:
        v=vf-100
        vf=vf-v
print(vf)        
     