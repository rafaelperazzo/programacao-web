# -*- coding: utf-8 -*-
def degrais(a):
    soma=0
    degrau=0
    for i in range(o,len(a)-1,1):
        soma=(a[i]-a[i+1])
        if soma<0:
            soma=soma*(-1)
        if soma>degrau:
            degrau=soma
    return degrau 
h=