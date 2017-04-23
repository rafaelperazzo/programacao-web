# -*- coding: utf-8 -*-
import math

CV=int(input('Digite o n de vit do cor:'))
CE=int(input('Digite o n de empates do cor:'))
CS=int(input('Digite o saldo de gols do cor:'))

FV=int(input('Digite o n de vit do fla:'))
FE=int(input('Digite o n de empates do fla:'))
FS=int(input('Digite o saldo de gols do fla:'))


v1=CV*3+CE*1
v2-FV*3+FE*1

if v1>v2:
    print ('C')
    
elif v1<v2:
    print ('F')
    
else: 
    if CS>FS:
        print ('C')
        
    elif CS<FS:
        print ('F')
        
    else:
        print ('=')
        


