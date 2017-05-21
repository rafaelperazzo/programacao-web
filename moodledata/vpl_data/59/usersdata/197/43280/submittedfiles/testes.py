# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite n:'))
a=int(input('Digite a:'))
b=int(input('Digite b:'))
cont=0
cm=0
while cont<n:
    if cm%a==0 or cm%b==0:
        print(cm)
        cont=cont+1
    cm=cm+1