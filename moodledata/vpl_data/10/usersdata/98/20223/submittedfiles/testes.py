# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
#DEFININDO A FUNÇÃO
def somaLinhas(a):
    soma=[]
    for i in range(0,a.shape(0),1):
        soma.append(sum(a[i,:]))
    return soma