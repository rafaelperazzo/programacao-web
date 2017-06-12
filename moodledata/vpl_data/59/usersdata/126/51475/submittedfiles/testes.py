# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO





def feliz(n):
    while q!=0:
        q=q//10
        cont=cont+1
        for i in rtange(1,cont+1,1):
            soma=0
            while n>0:
                p=n%10
                n=n//10
                soma=soma+p**2
            n=soma
            i=i+1
    if n==1:
        return(True)
    else:
        return(False)
n=int(input('digite:')
if feliz(soma):
    print('sim')
else:
    print('nao')