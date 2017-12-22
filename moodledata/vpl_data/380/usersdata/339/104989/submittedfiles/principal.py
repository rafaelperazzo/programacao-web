# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
#from minha_bib import *

a=int(input('a: '))
b=int(input('b: '))

da=0
db=0

while a>=1:
    da+=1
    a=a//10
while b>0:
    db+=1
    b=b//10
    
print('inteiro a: %d' %da)
print('inteiro b: %d' %db)

