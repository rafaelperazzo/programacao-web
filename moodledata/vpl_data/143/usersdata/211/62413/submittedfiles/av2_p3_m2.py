# -*- coding: utf-8 -*-
def degrais(A):
    Soma=0
    Degrau=0
    for i in range(0,len(A)-1,1):
        Soma=(A[i]-A[i+1])
        if Soma<0:
            Soma=Soma*(-1)
        if Soma>Degrau:
            Degrau=Soma
    return Degrau

         
