# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO





def feliz(n):
    q=n
    p=0
    i=0
    cont=0
    while q!=0:
        q=q//10
        cont=cont+1
        for i in range(1,cont+1,1):
            soma=0
            while n>0:
                p=n%10
                n=n//10
                soma=soma+p**2
            n=soma
            i=i+1
    if soma==1:
        return(True)
    else:
        return(False)
        
f=int(input('digite o valor a ser testado:'))

if feliz(f):
    print('sim')
else:
    print('nao')