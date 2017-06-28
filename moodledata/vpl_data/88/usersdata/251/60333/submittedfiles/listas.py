# -*- coding: utf-8 -*-
def degrau(lista):
    degraus=[]
    iten=0
    for i in range(1,len(lista),1):
        iten=abs(lista[i]-lista[i-1]
        degraus.append(iten)
    maiorDegrau=max(degraus)
    return(maiorDegrau)

