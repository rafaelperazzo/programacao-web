# -*- coding: utf-8 -*-
import math
cv=int(input('digite cv:'))
ce=int(input('digite ce:'))
cs=int(input('digite cs:'))
fv=int(input('digite fv:'))
fe=int(input('digite fe:'))
fs=int(input('digite fs:'))
pcv=cv*3
pfv=fv*3
if pcv+ce>pfv+fe:
    print('C')
elif pcv+ce<pfv+fe:
    print('F')
elif pcv+ce==pfv+fe:
    print('=')
    
