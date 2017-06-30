# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
def digitos(n):
    a=[]
    while n>=0:
        if n>=10:
            digito=n%10
            a.append(digitos)
        else:
            a.append(n)
        n=n//10
        return(a)
    
    