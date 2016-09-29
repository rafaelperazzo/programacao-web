# -*- coding: utf-8 -*-
from __future__ import division
import math

cv= input('Vitória time c: ')
ce= input('Empate time c: ')
cs= input('Saldo time c: ')
fs= input('Vitória time f: ')
fe: input('Empate time f: ')
fs: input('Saldo time f: ')

pc= (cv*3)+(ce*1)
pf= (fv*3)+(fe*1)

if pc>pf:
    print('C')
elif pc<pf:
    print('F')
else:
    print('=')