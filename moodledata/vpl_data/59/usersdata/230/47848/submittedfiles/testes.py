# -*- coding: utf-8 -*-
import math
n=int(input('Digite n:'))
i=1
while i*(i+1)*(i+2)>n:
    i=i+1
if i*(i+1)*(i+2)==n:
    print('s')
else:
    print('n')
    

    