# -*- coding: utf-8 -*-
import math

m=int(input('Digite a quantidade de termos:'))

i=0
soma=0
denominador=1

while i<=m:
        termo=4/(denominador)*(denominador+1)*denominador+2
        soma=soma+1
        if soma%2==0:
            geral=geral+termo
        if soma%2==1:
            geral=geral-termo
            

print('%.6f'%geral)
    
