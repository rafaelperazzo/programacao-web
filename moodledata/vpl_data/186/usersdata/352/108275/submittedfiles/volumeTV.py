 -*- coding: utf-8 -*-
 
 Vo=int(input('Volume inicial: '))
 modif=int(input('Quantidade de modificações: '))
 
 for i in range(0,modif,1):
    m=int(input('Modificação: '))
    Vo=(Vo+m)
    if(Vo>100):
        Vo=100
    if(Vo<0):
        V0=0
print(Vo)
    