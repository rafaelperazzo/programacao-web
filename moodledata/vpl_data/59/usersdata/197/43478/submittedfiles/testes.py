# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('digite n:'))
a=int(input('digite a:'))
b=int(input('digite b:'))
cont=0
multiplo=1
while cont<n:
    if multiplo%a==0 or multiplo%b==0:
        print(multiplo)
        cont=cont+1
        multiplo=multiplo+1