# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite a: ')

b = input('Digite b: ')

da =  10

db =  10

while a>da  :

    da = da +  10

    a = a//da 

while b>db  :

    db = db + 10 

    b = b//db 

 

print('Quantidade de dígitos de a: %d' %(a)  )

print('Quantidade de dígitos de b: %d' %(b)  )