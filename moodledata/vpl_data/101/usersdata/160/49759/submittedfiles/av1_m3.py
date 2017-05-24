# -*- coding: utf-8 -*-
import math

m=int(input('Digite a quantidade de termos:'))

i=0
soma=0
denominador=2
geral=0
termo=0


for i in range(0,m,1):
        termo=4/((denominador)*(denominador+1)*(denominador+2))
        denominador=denominador+1
        soma=soma+1
        if soma%2==0:
            geral=geral-termo
        if soma%2==1:
            geral=geral+termo
            
print('%.6f'%geral)
    
