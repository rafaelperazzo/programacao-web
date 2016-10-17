# -*- coding: utf-8 -*-
from __future__ import division
#COMECE AQUI ABAIXO
s = input ('Digite a senha:')
senha = 456
while s!=senha:
    s=input ('Digite a senha:')
    if senha ==s :
        print 'Bem vindo'