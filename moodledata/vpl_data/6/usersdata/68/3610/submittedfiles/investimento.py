# -*- coding: utf-8 -*-
from __future__ import division

#ENTRADA:
vi1=input ('Digite o valor do investimento inicial no ano 1:') 
tc1=input ('Digite a taxa de crescimento no ano 1 em casas decimais:')

InvAno1= vi1 + tc1*vi1

print ('%.2f' %InvAno1)
