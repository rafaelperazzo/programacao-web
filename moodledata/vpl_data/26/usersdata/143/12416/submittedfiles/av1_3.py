# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite a: ')

b = input('Digite b: ')

da =  1

db =  1

while a>da  :

    da = da +  1

    a = a//da 

while b>db  :

    db = db + 1 

    b = b//db 

 

print('Quantidade de dígitos de a: %d' %(a)  )

print('Quantidade de dígitos de b: %d' %(b)  )