# -*- coding: utf-8 -*-
#COMECE AQUI 
salarioh=float(input('quanto vc ganha por hora?: '))
salariob=salarioh*30
ir=salariob-(salariob*0.11)
inss=salariob-(salariob*0.08)
sindicato=salariob-(salariob*0.05)
salariol=salariob-ir-inss-sindicato
print('+'salariob)
print('-'ir)
print('-'inss)
print('-'sindicato)
print('