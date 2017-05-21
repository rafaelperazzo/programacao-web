# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite o número de termos: '))
cont=0
for i in range(1,n+1,1):
    if i/2==1:
        cont=cont+i
    else:
        cont=cont
print(cont)

    
