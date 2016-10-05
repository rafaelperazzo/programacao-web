# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Digite a quantidade de termos:')

produto=1

for i in range(1,(n/n**2),1):
    print('%.5f '%produto)
    
         produto=produto*i