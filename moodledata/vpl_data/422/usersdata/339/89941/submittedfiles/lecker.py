# -*- coding: utf-8 -*-
import math



n1=int(input('n1: '))
n2=int(input('n2: '))
n3=int(input('n3: '))
n4=int(input('n4: '))

Lista=[n1,n2,n3,n4]

 
for i in Lista:
    if Lista[0]>Lista[1] and Lista[2]>Lista[1] and Lista[2]>Lista[3]:
        print('N')
    elif i==Lista[0] and i==Lista[1] and i==Lista[2] and i==Lista[3]: 
        print('N')
    elif Lista[0]<Lista[1] and Lista[2]<Lista[1] and Lista[2]<Lista[3]:
        print('N')
    elif Lista[0]>Lista[1] and Lista[2]<Lista[3]:
        print('N')
    elif Lista[i]<Lista[i:-1]:
        print('N')
    else:
        print('S')
    break
        







