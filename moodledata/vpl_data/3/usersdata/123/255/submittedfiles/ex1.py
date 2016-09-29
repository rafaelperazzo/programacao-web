# -*- coding: utf-8 -*-
from __future__ import division
a= input ('Digite um valor para a:')
b= input ('Digite um valor para b:')
c= input ('Digite um valor para c:')

delta= (b**2) - (4*a*c)

if delta>=0:
    x1= (-b + ((delta)**(1/2)))/2*a
    x2= (-b - ((delta)**(1/2)))/2*a
    print('%.2f' %x1)
    print('%.2f' %x2)

else:
    print ('Não existem raízes reais ara essa equação')