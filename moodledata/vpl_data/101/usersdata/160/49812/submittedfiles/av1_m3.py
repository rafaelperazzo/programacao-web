# -*- coding: utf-8 -*-
import math

m=int(input('Digite a quantidade de termos:'))

i=0
cont=0
denominador=2
geral=0
termo=0


for i in range(0,m,1):
        termo=4/((denominador)*(denominador+1)*(denominador+2))
        denominador=denominador+2
        cont=cont+1
        if cont%2==0:
            geral=geral-termo
        if cont%2==1:
            geral=geral+termo

total=63+geral            
print('%.6f'%total)
    
