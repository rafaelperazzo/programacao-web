# -*- coding: utf-8 -*-
from __future__ import division
import math 
Sh=input('Digite o valor que você ganha por hora: ')
Nh=input('Digite o número de horas trabalhadas por mês: ')
salariobr=(Sh*Nh)
INSS=(salariobr*0.08)
sind=(salariobr*0.05)
IR=(salariobr*0.11)
salarioliq=(salariobr-INSS-sind-IR)
print salarioliq
    