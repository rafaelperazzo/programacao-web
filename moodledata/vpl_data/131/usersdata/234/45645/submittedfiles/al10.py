# -*- coding: utf-8 -*-
v=int(input('digite o número dos termos:'))
i=0
numerador=2
denominaador=1
produto=1
while i<=(v-1):
    produto=produto*numerador/denominador
    if i%2==1:
        numerador=numerador+2
    else:
        denominador=denominador+2
    i=i+1
produto=produto*2
    print('%.5f'%produto)
        

