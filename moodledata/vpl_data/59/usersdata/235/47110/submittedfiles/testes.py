# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('digiti n:'))
i=0
soma=0
while n>0:
    m=n%10
    soma=soma+m*(2**i)
    print(soma)
    

    