# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite a: ')

b = input('Digite b: ')

da =  0

db =  0

while a>da  :

    da = da + 100

    a = a//da 

while b>db  :

    db = db + 100 

    b = b//db 

 

print('Quantidade de dígitos de a: %d' %(da)  )

print('Quantidade de dígitos de b: %d' %(db)  )