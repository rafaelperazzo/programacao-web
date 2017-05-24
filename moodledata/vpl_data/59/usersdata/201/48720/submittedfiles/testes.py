# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=float(input('Digite um valor:'))
if a==5 or a==200 or a==500:
    print(a)
elif a>500 and a<1000:
    print('Sim')
    if a<500 or a>1000:
        print('Fora')