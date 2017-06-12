# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('digite:')
p=0
q=n
cont=0
i=0
def falez(n):
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
if feliz(n):
    print('sim')
else:
    print('nao')