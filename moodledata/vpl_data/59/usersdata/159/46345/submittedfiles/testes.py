# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
k=int(input('Digite k:'))
pi=4
denominador=3
for i in range (1,k+1,1):
    a=4/denominador
    if i%2!=0:
        pi=pi-a
    else:
        pi=pi+a
print(pi)        

 

    